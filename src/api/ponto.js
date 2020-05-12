import http from "./http";

export default {
    postTurno(dia, chegada, saida, saida_almoco, entrada_almoco, presente, id_Funcionario){
        return http.post("/api/turno-management/", {
            dia,
            chegada,
            saida,
            saida_almoco,
            entrada_almoco,
            presente,
            id_Funcionario
        });
    },
    getTurno(){
        return http.get("/api/turno/");
    }
}