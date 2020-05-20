import auth from "@/modules/auth/api";
import {CADAS_BEGIN, CADAS_END, SET_SAIDA, SET_CHEGADA, SET_LAST_USER} from "./types";

export default {
    getLastUser({ commit }) {
        // eslint-disable-next-line no-debugger
        debugger;
        return auth
            .getLastUser()
            .then(({ data }) => {
            commit(SET_LAST_USER, data);
            })
    },
    cadastrar({ commit },{username, email, first_name, last_name, password}) {
        commit(CADAS_BEGIN);
            return auth
                .cadastrar(username, email, first_name, last_name, password)
                .finally(() => commit(CADAS_END))
    },

    // eslint-disable-next-line no-unused-vars
    setHorario({ commit }, { hora_chegada, hora_saida, user }) {
        // eslint-disable-next-line no-debugger
        debugger;
            return auth
                .setHorario(hora_chegada, hora_saida, user)
    },
    setChegada({ commit }, date) {
    commit(SET_CHEGADA, date);
    },
    setSaida({ commit }, date) {
    commit(SET_SAIDA, date);
  },
}