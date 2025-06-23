package com.globalenrollment.usercreation.controller;

import com.globalenrollment.usercreation.model.StudentUser;
import com.globalenrollment.usercreation.repository.StudentUserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.UUID;

@RestController
@RequestMapping("/users")
public class StudentUserController {

    @Autowired
    private StudentUserRepository repository;

    @PostMapping
    public StudentUser createUser(@RequestBody StudentUser user) {
        user.setId(UUID.randomUUID());
        user.setRegistrationDate(java.time.LocalDateTime.now());
        return repository.save(user);
    }
}
