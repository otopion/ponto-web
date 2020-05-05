import { CADAS_BEGIN, CADAS_END, SET_USER_CADAS, SET_CHEGADA, SET_SAIDA } from "./types";

export default {
  [CADAS_BEGIN](state) {
    state.setCadastro = true;
  },
  [CADAS_END](state) {
    state.setCadastro = false;
  },
  [SET_USER_CADAS](state, user) {
    state.cadas_user = user;
  },
  [SET_CHEGADA](state, date){
    state.hora_chegada = date
  },
  [SET_SAIDA](state, date){
    state.hora_saida = date
  }
};