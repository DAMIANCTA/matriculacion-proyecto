CREATE TABLE IF NOT EXISTS enrollments (
    id UUID PRIMARY KEY,
    student_id UUID NOT NULL,
    section_id UUID NOT NULL,
    enrollment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR DEFAULT 'ACTIVE'
);

CREATE TABLE IF NOT EXISTS enrollment_logs (
    id UUID PRIMARY KEY,
    enrollment_id UUID NOT NULL,
    student_id UUID NOT NULL,
    section_id UUID NOT NULL,
    action VARCHAR DEFAULT 'CREATED',
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source_ip VARCHAR,
    details VARCHAR
);
