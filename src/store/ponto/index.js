import actions from "./actions";
import getters from "./getters"
import mutations from "./mutations";

const initialState = {
    dia: "",
    turno: [],
    pesquisa: "",
    delete: "",
    deleto: false,
    edit: null,
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