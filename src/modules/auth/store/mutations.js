import { LOGIN_BEGIN, LOGIN_END, SET_USER, SET_FUNCIONARIO, SET_TURNO } from "./types";

export default {
  [LOGIN_BEGIN](state) {
    state.authenticating = true;
  },
  [LOGIN_END](state) {
    state.authenticating = false;
  },
  [SET_USER](state, user) {
    state.user = user;
  },
  [SET_FUNCIONARIO](state, funcionario){
    state.funcionario = funcionario;
  },
      [SET_TURNO](state, data){
        state.turno = data;
    }
};
