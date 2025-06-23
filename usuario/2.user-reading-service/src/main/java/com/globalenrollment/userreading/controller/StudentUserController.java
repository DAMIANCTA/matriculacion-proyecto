package com.globalenrollment.userreading.controller;

import com.globalenrollment.userreading.model.StudentUser;
import com.globalenrollment.userreading.repository.StudentUserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/users")
public class StudentUserController {

    @Autowired
    private StudentUserRepository repository;

    @GetMapping
    public List<StudentUser> getAllUsers() {
        return repository.findAll();
    }

    @GetMapping("/<built-in function id>")
    public StudentUser getUserById(@PathVariable UUID id) {
        return repository.findById(id).orElse(null);
    }
}
