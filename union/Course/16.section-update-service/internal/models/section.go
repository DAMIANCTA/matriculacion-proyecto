package models

import "time"

type Section struct {
	ID              string    `json:"id" db:"id"`
	SubjectID       string    `json:"subject_id" db:"subject_id"`
	Name            string    `json:"name" db:"name"`
	TotalCapacity   int       `json:"total_capacity" db:"total_capacity"`
	CurrentCapacity int       `json:"current_capacity" db:"current_capacity"`
	Schedule        string    `json:"schedule" db:"schedule"`
	CreationDate    time.Time `json:"creation_date" db:"creation_date"`
}
