
package com.globalenrollment.login;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import java.util.Optional;


@RestController
@RequestMapping("/login")
public class LoginController {

    @Autowired
    private UserRepository userRepository;

   @PostMapping
public ResponseEntity<Object> login(@RequestBody LoginRequest request) {
    Optional<User> userOpt = userRepository.findByUsernameAndPassword(
        request.getUsername(), request.getPassword()
    );

    if (userOpt.isPresent()) {
        return ResponseEntity.ok().body(userOpt.get());
    } else {
        return ResponseEntity.status(401).body("Credenciales inválidas");
    }
}

}
