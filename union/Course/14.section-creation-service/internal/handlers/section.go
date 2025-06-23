package handlers

import (
	"fmt"
	"net/http"
	"section/internal/models"

	"github.com/gin-gonic/gin"
	"github.com/google/uuid"
	"github.com/jmoiron/sqlx"
)

func CreateSection(db *sqlx.DB) gin.HandlerFunc {
	return func(c *gin.Context) {
		var section models.Section
		if err := c.ShouldBindJSON(&section); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
			return
		}

		// Generar UUID si no viene en el JSON
		if section.ID == "" {
			section.ID = uuid.New().String()
		}

		// Validación del subject_id llamando al microservicio Subjects
		subjectURL := fmt.Sprintf("http://subject-reading-service:3007/subjects/%s", section.SubjectID)
		resp, err := http.Get(subjectURL)
		if err != nil || resp.StatusCode != http.StatusOK {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Subject ID is invalid or not found"})
			return
		}
		defer resp.Body.Close()

		// Insertar la sección solo si el subject existe
		query := `INSERT INTO sections (id, subject_id, name, total_capacity, current_capacity, schedule, creation_date)
                  VALUES (:id, :subject_id, :name, :total_capacity, :current_capacity, :schedule, :creation_date)`
		_, err = db.NamedExec(query, &section)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Database insert failed"})
			return
		}

		c.JSON(http.StatusOK, gin.H{"message": "Section created successfully"})
	}
}
