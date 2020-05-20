import {CADAS_BEGIN, CADAS_END, SET_CHEGADA, SET_LAST_USER, SET_SAIDA} from "./types";

export default {
  [CADAS_BEGIN](state) {
    state.setCadastro = true;
  },
  [CADAS_END](state) {
    state.setCadastro = false;
  },
  [SET_CHEGADA](state, date){
    state.hora_chegada = date;
  },
  [SET_SAIDA](state, date){
    state.hora_saida = date;
  },
  [SET_LAST_USER](state, date){
    state.lastUser = date
  }
};