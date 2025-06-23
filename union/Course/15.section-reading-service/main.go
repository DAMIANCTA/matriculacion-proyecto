package main

import (
	"fmt"
	"log"
	"os"
	"section-reading-service/handlers"

	"github.com/gin-gonic/gin"
	"github.com/jmoiron/sqlx"
	_ "github.com/lib/pq"
)

func main() {
	dbUser := os.Getenv("DB_USER")
	dbPassword := os.Getenv("DB_PASSWORD")
	dbHost := os.Getenv("DB_HOST")
	dbName := os.Getenv("DB_NAME")

	dsn := fmt.Sprintf("user=%s password=%s host=%s dbname=%s sslmode=disable", dbUser, dbPassword, dbHost, dbName)
	db, err := sqlx.Connect("postgres", dsn)
	if err != nil {
		log.Fatalln("Error al conectar a la base de datos:", err)
	}

	router := gin.Default()
	router.GET("/sections", handlers.GetAllSections(db))
	router.GET("/sections/:id", handlers.GetSectionByID(db))

	router.Run(":3011")
}
