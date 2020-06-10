import * as types from "./types";
import ponto from "../../api/ponto";

export default {
    setDia({ commit }, data){
        commit(types.SET_DIA, data);
    },
    setPesquisa({ commit }, data){
        commit(types.SET_PESQUISA, data)
    },
    setDelete({ commit }, data){
      commit(types.DELETE_TURNO, data)
    },
    abrirEdit({ commit }, item){
        commit(types.SET_EDIT, item)
    },
    getTurno({ commit }){
        commit(types.SET_LOADING_TURNO, true);
        return ponto
          .getTurno()
          .then(response => commit(types.SET_TURNO, response.data))
          .finally(() => commit(types.SET_LOADING_TURNO, false));
    },
    deleteTurno(id){
        return ponto
            .deleteTurno(id)
    },
    postTurno({ commit }, { data, hora_chegada, hora_saida, saida_almoco, entrada_almoco, presente, id_funcionario }) {
        return ponto
            .postTurno(data, hora_chegada, hora_saida, saida_almoco, entrada_almoco, presente, id_funcionario)
                 .then(() => {
                    commit(types.SET_HAS_CHANGES, false);
                  })
                  .finally(() =>
                    setTimeout(() => {
                      commit(types.SET_CHANGING_DATA, false);
                    }, 1000)
      );
    },
    // eslint-disable-next-line no-unused-vars
    editTurno({ commit }, { data, hora_chegada, hora_saida, saida_almoco, entrada_almoco, presente, id_funcionario, id }){
        return ponto
            .editTurno(data, hora_chegada, hora_saida, saida_almoco, entrada_almoco, presente, id_funcionario, id)
    },
}