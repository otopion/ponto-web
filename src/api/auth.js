import http from "./http";

export default {
  login(email, senha, rememberMe) {
    return http.post("/api/auth/funcionario/", {
      email,
      senha,
      remember_me: rememberMe
    });
  },
};