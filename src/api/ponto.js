import http from "./http";

export default {
    getTurno(){
      return http.get()("/api/turno/");
    },
    postTurno(){
        return http.post("api/turno-management/")
    }
}