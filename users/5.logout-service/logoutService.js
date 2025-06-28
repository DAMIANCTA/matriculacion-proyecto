const service = {
  LogoutService: {
    LogoutPort: {
      logoutUser(args) {
        console.log("Petición de logout recibida:", args);
        return {
          message: "Sesión cerrada correctamente"
        };
      }
    }
  }
};

module.exports = service;
