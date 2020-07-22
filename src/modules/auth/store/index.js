import { isProduction } from "@/utils";
import actions from "./actions";
import mutations from "./mutations";
import getters from "./getters";

const initialState = {
  authenticating: false,
  user: null,
  funcionario: [],
};

if (isProduction) {
  initialState.user = window.PONTO;
}

export default {
  namespaced: true,
  modules: {
    acconts: require("./acconts").default
  },
  state: initialState,
  actions,
  mutations,
  getters
};
