package com.globalenrollment.userreading.controller;

import com.globalenrollment.userreading.model.StudentUser;
import com.globalenrollment.userreading.repository.StudentUserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.ResponseEntity;


import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/users")
public class StudentUserController {

    @Autowired
    private StudentUserRepository repository;

    // Acepta /users y /users/
    @GetMapping({"", "/"})
    public List<StudentUser> getAllUsers() {
        return repository.findAll();
    }

    @GetMapping("/{id}")
    public ResponseEntity<StudentUser> getUserById(@PathVariable UUID id) {
        return repository.findById(id)
            .map(ResponseEntity::ok)
            .orElse(ResponseEntity.notFound().build());
    }


}
