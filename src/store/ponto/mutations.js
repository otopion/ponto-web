import {SET_DIA, SET_TURNO} from "./types";

export default {
    [SET_DIA](state, data){
        state.dia = data;
    },
    [SET_TURNO](state, data){
        state.turno = data;
    }
}