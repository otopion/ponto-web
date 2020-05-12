import {SET_DIA, SET_PESQUISA, SET_TURNO} from "./types";

export default {
    [SET_DIA](state, data){
        state.dia = data;
    },
    [SET_TURNO](state, data){
        state.turno = data;
    },
    [SET_PESQUISA](state, data){
        state.pesquisa = data
    }
}