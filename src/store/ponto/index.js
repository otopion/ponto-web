import actions from "./actions";
import getters from "./getters"
import mutations from "./mutations";

const initialState = {
      dia: "",
      turno: null,
      pesquisa: "",
};

export default {
    namespaced: true,
    state: initialState,
    actions,
    getters,
    mutations,
}