package models

type Section struct {
    ID              string `db:"id" json:"id"`
    SubjectID       string `db:"subject_id" json:"subject_id"`
    Name            string `db:"name" json:"name"`
    TotalCapacity   int    `db:"total_capacity" json:"total_capacity"`
    CurrentCapacity int    `db:"current_capacity" json:"current_capacity"`
    Schedule        string `db:"schedule" json:"schedule"`
    CreationDate    string `db:"creation_date" json:"creation_date"`
}
