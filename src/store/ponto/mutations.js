import * as types from "./types";
import moment from 'moment';

export default {
    [types.SET_DIA](state, data){
        state.dia = data;
    },
    [types.SET_TURNO](state, data){
        state.turno = data;
        for(let i = 0; state.turno[i] != null; i++) {
            state.turno[i].data = state.turno[i].data.split('-').reverse().join('/');
        }
        for(let i=0; state.turno[i] != null; i++){
            if(state.turno[i].presente === true )
                state.turno[i].presente = "Presente";
            if(state.turno[i].presente === false )
                state.turno[i].presente = "Ausente";
        }
    },
    [types.SET_PESQUISA](state, data){
        state.pesquisa = data
    },
    [types.DELETE_TURNO](state, data){
        state.delete = data
    },
    [types.SET_EDIT](state, item){
        state.edit.data = item.data.split('/').reverse().join('-');
        state.edit.hora_chegada = moment(item.hora_chegada, 'HH:mm').format('HH:mm');
        state.edit.hora_saida = moment(item.hora_saida, 'HH:mm').format('HH:mm');
        state.edit.saida_almoco = moment(item.saida_almoco, 'HH:mm').format('HH:mm');
        state.edit.entrada_almoco = moment(item.entrada_almoco, 'HH:mm').format('HH:mm');
        state.edit.presente = item.presente !== "Ausente";
        state.edit.id_funcionario = item.id_Funcionario;
        state.edit.id = item.id;
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
    [types.LIMPA_CAMPOS_EDIT](state){
        state.edit.hora_chegada = "HH:mm";
        state.edit.hora_saida = "HH:mm";
        state.edit.saida_almoco = "HH:mm";
        state.edit.entrada_almoco  = "HH:mm";
    },
    [types.LIMPA_DADOS_EDIT](state){
        state.edit.data = "";
        state.hora_chegada = "";
        state.edit.hora_saida = null;
        state.edit.saida_almoco = null;
        state.edit.entrada_almoco  = null;
        state.edit.presente = false;
    }
}