import http from "./http";

export default {
    postTurno(data, hora_chegada, hora_saida, saida_almoco, entrada_almoco, presente, id_Funcionario){
        return http.post("/api/turno-management/", {
            data,
            hora_chegada,
            hora_saida,
            saida_almoco,
            entrada_almoco,
            presente,
            id_Funcionario,
        });
    },

    editTurno(data, hora_chegada, hora_saida, saida_almoco, entrada_almoco, presente, id_Funcionario, id){
        return http.put("/api/turno-management/"+JSON.stringify(id)+"/", {
            data,
            hora_chegada,
            hora_saida,
            saida_almoco,
            entrada_almoco,
            presente,
            id_Funcionario,
        });
    },
    deleteTurno(id){
        return http.delete("/api/turno-management/"+JSON.stringify(id.state.delete)+"/");
    },
    getTurno(){
        return http.get("/api/turno/");
    }
}