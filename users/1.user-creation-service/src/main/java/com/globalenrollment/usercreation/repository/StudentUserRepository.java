package com.globalenrollment.usercreation.repository;

import com.globalenrollment.usercreation.model.StudentUser;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.UUID;

public interface StudentUserRepository extends JpaRepository<StudentUser, UUID> {}
