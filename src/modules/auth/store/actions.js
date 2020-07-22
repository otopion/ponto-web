import { LOGIN_BEGIN, LOGIN_END, SET_USER, SET_FUNCIONARIO } from "./types";
import auth from "../api";

export default {
  login({ commit }, { username, password, rememberMe }) {
    commit(LOGIN_BEGIN);
    return auth
      .login(username, password, rememberMe)
      .then(({ data }) => commit(SET_USER, data))
      .finally(() => commit(LOGIN_END));
  },
  logout({ commit }) {
    return auth.logout().finally(() => commit(SET_USER, null), commit(SET_FUNCIONARIO, null));
  },
  getFuncionario({ commit }) {
    return auth
    .getFuncionario()
        .then(({ data }) => {
          commit(SET_FUNCIONARIO, data);
        })
  },
  init({ commit }) {
    return new Promise(resolve => {
        auth
          .getUser()
          .then(({ data }) => {
            commit(SET_USER, data);
          })
          .finally(() => {
            resolve();
          });
    });
  }
};
