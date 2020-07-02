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
        hora_chegada: "",
        hora_saida: "",
        saida_almoco: "",
        entrada_almoco: "",
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