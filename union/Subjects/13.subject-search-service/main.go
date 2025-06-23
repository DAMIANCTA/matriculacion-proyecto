package main

import (
    "database/sql"
    "fmt"
    "log"
    "os"

    "github.com/gofiber/fiber/v2"
    _ "github.com/lib/pq"
)

func main() {
    app := fiber.New()

    db, err := sql.Open("postgres", fmt.Sprintf(
        "host=%s user=%s password=%s dbname=%s sslmode=disable",
        os.Getenv("DB_HOST"), os.Getenv("DB_USER"), os.Getenv("DB_PASSWORD"), os.Getenv("DB_NAME"),
    ))
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    app.Post("/webhook/subject-search", func(c *fiber.Ctx) error {
        var query struct {
            Name     string `json:"name"`
            Credits  int    `json:"credits"`
            Duration string `json:"duration"`
        }

        if err := c.BodyParser(&query); err != nil {
            return c.Status(400).JSON(fiber.Map{"status": "error", "message": "Invalid request"})
        }

        sqlQuery := "SELECT * FROM subjects WHERE 1=1"
        args := []interface{}{}
        i := 1

        if query.Name != "" {
            sqlQuery += fmt.Sprintf(" AND name ILIKE $%d", i)
            args = append(args, "%"+query.Name+"%")
            i++
        }
        if query.Credits != 0 {
            sqlQuery += fmt.Sprintf(" AND credits = $%d", i)
            args = append(args, query.Credits)
            i++
        }
        if query.Duration != "" {
            sqlQuery += fmt.Sprintf(" AND duration = $%d", i)
            args = append(args, query.Duration)
            i++
        }

        rows, err := db.Query(sqlQuery, args...)
        if err != nil {
            return c.Status(500).JSON(fiber.Map{"status": "error", "message": err.Error()})
        }
        defer rows.Close()

        results := []map[string]interface{}{}
        for rows.Next() {
            var id, name, description, duration string
            var credits int
            if err := rows.Scan(&id, &name, &description, &credits, &duration); err != nil {
                continue
            }
            results = append(results, map[string]interface{}{
                "id": id, "name": name, "description": description,
                "credits": credits, "duration": duration,
            })
        }

        return c.JSON(fiber.Map{"status": "success", "data": results})
    })

    log.Fatal(app.Listen(":3009"))
}