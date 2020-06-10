import actions from "./actions";
import getters from "./getters"
import mutations from "./mutations";

const initialState = {
    turno: [],
    pesquisa: "",
    delete: "",
    deleto: false,
    edit: {
        data: "",
        hora_chegada: null,
        hora_saida: null,
        saida_almoco: null,
        entrada_almoco: null,
        presente: false,
        id_funcionario: null,
        id: null,
    },
    loadingTurno: false,
    hasChanges: false,
    changingData: false,
};

export default {
    namespaced: true,
    state: initialState,
    actions,
    getters,
    mutations,
}