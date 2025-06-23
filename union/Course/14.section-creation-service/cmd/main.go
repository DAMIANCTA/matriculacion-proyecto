package main

import (
	"log"
	"os"

	"github.com/gin-gonic/gin"
	"section/internal/handlers"
	"section/internal/database"
)

func main() {
	db, err := database.Connect()
	if err != nil {
		log.Fatalf("Database connection failed: %v", err)
	}
	defer db.Close()

	router := gin.Default()
	router.POST("/sections", handlers.CreateSection(db))
	port := os.Getenv("PORT")
	if port == "" {
		port = "3010"
	}
	router.Run(":" + port)
}
