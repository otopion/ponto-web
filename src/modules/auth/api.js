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
  getLastUser(){
      // eslint-disable-next-line no-debugger
      debugger;
      return http.get("/api/auth/last-user");
  },
  cadastrar(username, email, first_name, last_name, password){
    return http.post("/api/acconts/cadastrar/", {
      username,
      email,
      first_name,
      last_name,
      password
    })
  },
 setHorario(hora_chegada, hora_saida, user){
   // eslint-disable-next-line no-debugger
    debugger;
    return http.post("/api/funcionario-management/", {
      hora_chegada,
      hora_saida,
      user
    })
  },
  getFuncionario(){
     return http.get("/api/funcionario/");
  },
};
