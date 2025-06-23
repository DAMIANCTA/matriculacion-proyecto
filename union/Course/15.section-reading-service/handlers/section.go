package handlers

import (
	"net/http"
	"section-reading-service/models"

	"github.com/gin-gonic/gin"
	"github.com/jmoiron/sqlx"
)

func GetAllSections(db *sqlx.DB) gin.HandlerFunc {
	return func(c *gin.Context) {
		var sections []models.Section
		err := db.Select(&sections, "SELECT * FROM sections")
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": "Error al obtener secciones"})
			return
		}
		c.JSON(http.StatusOK, sections)
	}
}

func GetSectionByID(db *sqlx.DB) gin.HandlerFunc {
	return func(c *gin.Context) {
		id := c.Param("id")
		var section models.Section
		err := db.Get(&section, "SELECT * FROM sections WHERE id=$1", id)
		if err != nil {
			c.JSON(http.StatusNotFound, gin.H{"error": "Sección no encontrada"})
			return
		}
		c.JSON(http.StatusOK, section)
	}
}
