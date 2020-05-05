import actions from "./actions"
import mutations from "./mutations"

const initialState = {
  setCadastro: false,
  hora_saida: "",
  hora_chegada: "",
  cadas_user: null,
};


export default {
  state: initialState,
  actions,
  mutations
}