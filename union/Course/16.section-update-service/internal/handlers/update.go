package handlers

import (
	"net/http"
	"section-update-service/internal/models"

	"github.com/gin-gonic/gin"
	"github.com/jmoiron/sqlx"
)

func UpdateSection(db *sqlx.DB) gin.HandlerFunc {
	return func(c *gin.Context) {
		var section models.Section
		if err := c.ShouldBindJSON(&section); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		query := `UPDATE sections SET 
			subject_id = :subject_id,
			name = :name,
			total_capacity = :total_capacity,
			current_capacity = :current_capacity,
			schedule = :schedule
			WHERE id = :id`

		_, err := db.NamedExec(query, &section)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Database update failed"})
			return
		}

		c.JSON(http.StatusOK, gin.H{"message": "Section updated successfully"})
	}
}
