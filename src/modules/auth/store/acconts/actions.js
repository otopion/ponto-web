import auth from "@/modules/auth/api";
import { CADAS_BEGIN, CADAS_END, SET_USER_CADAS, SET_SAIDA, SET_CHEGADA } from "./types";

export default {
    cadastrar({ commit },{username, email, first_name, last_name, password}) {
        commit(CADAS_BEGIN);
            return auth
                .cadastrar(username, email, first_name, last_name, password)
                .then(({data}) => commit(SET_USER_CADAS, data))
                .finally(() => commit(CADAS_END))
    },
    setHorario({ commit }, {user, hora_chegada, hora_saida}) {
            return auth
                .setHorario(user, hora_chegada, hora_saida)
                .finally(() => commit(CADAS_END))
    },
    setChegada({ commit }, date) {
    commit(SET_CHEGADA, date);
    },
    setSaida({ commit }, date) {
    commit(SET_SAIDA, date);
  },
}