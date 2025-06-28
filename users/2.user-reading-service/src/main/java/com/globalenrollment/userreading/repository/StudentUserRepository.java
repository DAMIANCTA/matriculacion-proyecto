package com.globalenrollment.userreading.repository;

import com.globalenrollment.userreading.model.StudentUser;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface StudentUserRepository extends JpaRepository<StudentUser, UUID> {}
