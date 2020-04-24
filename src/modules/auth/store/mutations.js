import { LOGIN_BEGIN, LOGIN_END, SET_USER } from "./types";

export default {
  [LOGIN_BEGIN](state) {
    state.authenticating = true;
  },
  [LOGIN_END](state) {
    state.authenticating = false;
  },
  [SET_USER](state, user) {
    state.user = user;
  }
};
