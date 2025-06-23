
package com.globalenrollment.login;

import jakarta.persistence.*;
import java.time.LocalDateTime;
import java.util.UUID;

@Entity
@Table(name = "student_users")
public class User {

    @Id
    private UUID id;

    private String firstName;
    private String email;
    private String country;
    private LocalDateTime registrationDate;
    private String username;
    private String password;
    private String role;
    private LocalDateTime lastLogin;

    public User() {}

    public UUID getId() { return id; }
    public String getFirstName() { return firstName; }
    public String getEmail() { return email; }
    public String getCountry() { return country; }
    public LocalDateTime getRegistrationDate() { return registrationDate; }
    public String getUsername() { return username; }
    public String getPassword() { return password; }
    public String getRole() { return role; }
    public LocalDateTime getLastLogin() { return lastLogin; }

    public void setId(UUID id) { this.id = id; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public void setEmail(String email) { this.email = email; }
    public void setCountry(String country) { this.country = country; }
    public void setRegistrationDate(LocalDateTime registrationDate) { this.registrationDate = registrationDate; }
    public void setUsername(String username) { this.username = username; }
    public void setPassword(String password) { this.password = password; }
    public void setRole(String role) { this.role = role; }
    public void setLastLogin(LocalDateTime lastLogin) { this.lastLogin = lastLogin; }
}
