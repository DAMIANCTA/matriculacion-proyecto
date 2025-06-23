package main

import (
	"log"
	"os"
	"section-update-service/internal/db"
	"section-update-service/internal/handlers"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()
	database := db.ConnectDB()

	router.POST("/webhook/update-section", handlers.UpdateSection(database))

	port := os.Getenv("PORT")
	if port == "" {
		port = "3012"
	}
	log.Fatal(router.Run(":" + port))
}
