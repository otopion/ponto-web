import * as types from "./types";

export default {
    [types.SET_DIA](state, data){
        state.dia = data;
    },
    [types.SET_TURNO](state, data){
        state.turno = data

    },
    [types.SET_PESQUISA](state, data){
        state.pesquisa = data
    },
    [types.DELETE_TURNO](state, data){
        state.delete = data
    },
    [types.DELETO](state, data){
        state.deleto = data
    },
    [types.SET_EDIT](state, data){
        state.edit = data
    },
    [types.UPDATE_TURNO](state, turno){
        state.turno = state.turno + turno;
    },
    [types.SET_LOADING_TURNO](state, loading){
        state.loadingTurno = loading;
    },
    [types.SET_HAS_CHANGES](state, value) {
        state.hasChanges = value;
    },
    [types.SET_CHANGING_DATA](state, value) {
         state.changingData = value;
    },
    [types.SET_HOUR](state, value){
        state.hour = value;
    },
}