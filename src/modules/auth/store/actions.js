import { isProduction } from "@/utils";
import { LOGIN_BEGIN, LOGIN_END, SET_USER, SET_FUNCIONARIO } from "./types";
import auth from "../api";
import ponto from "../../../api/ponto";
import {SET_TURNO} from "../../../store/ponto/types";

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
  init({ commit }) {
    return new Promise(resolve => {
      if (isProduction) {
        resolve();
      } else {
        auth
          .getUser()
          .then(({ data }) => {
            commit(SET_USER, data);
          })
          .finally(() => {
            resolve();
          });
      }
      return new Promise(resolve => {
      if (isProduction) {
        resolve();
      } else {
        auth
          .getFuncionario()
          .then(({ data }) => {
            commit(SET_FUNCIONARIO, data);
          })
          .finally(() => {
            resolve();
          });
      }
      return new Promise(resolve => {
      if (isProduction) {
        resolve();
      } else {
        ponto
          .getTurno()
          .then(({ data }) => {
            commit(SET_TURNO, data);
          })
          .finally(() => {
            resolve();
          });
      }
    });
    });
    });
  }
};
