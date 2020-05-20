import {
    DELETE_TURNO,
    SET_DIA,
    SET_PESQUISA,
    SET_TURNO,
    DELETO,
    SET_EDIT,
    UPDATE_TURNO,
    SET_LOADING_TURNO, SET_HAS_CHANGES, SET_CHANGING_DATA
} from "./types";


export default {
    [SET_DIA](state, data){
        state.dia = data;
    },
    [SET_TURNO](state, data){
        state.turno = data

    },
    [SET_PESQUISA](state, data){
        state.pesquisa = data
    },
    [DELETE_TURNO](state, data){
        state.delete = data
    },
    [DELETO](state, data){
        state.deleto = data
    },
    [SET_EDIT](state, data){
        state.edit = data
    },
    [UPDATE_TURNO](state, turno){
        console.log("Update Turno Mutation");
        state.turno = state.turno + turno;
    },
    [SET_LOADING_TURNO](state, loading){
        state.loadingTurno = loading;
    },
    [SET_HAS_CHANGES](state, value) {
        state.hasChanges = value;
    },
    [SET_CHANGING_DATA](state, value) {
    state.changingData = value;
  },
}