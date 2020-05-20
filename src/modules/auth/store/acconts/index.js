import actions from "./actions"
import mutations from "./mutations"

const initialState = {
  setCadastro: false,
  hora_saida: "",
  hora_chegada: "",
  lasUser: null,
};


export default {
  state: initialState,
  actions,
  mutations
}