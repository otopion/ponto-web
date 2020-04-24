import http from "@/api/http";

export default {
  login(username, password, rememberMe) {
    return http.post("/api/auth/login/", {
      username,
      password,
      remember_me: rememberMe
    });
  },
  logout() {
    return http.post("/api/auth/logout/", {});
  },
  getUser() {
    return http.get("/api/auth/user/");
  },

};
