import { isProduction } from "@/utils";
import actions from "./actions";
import mutations from "./mutations";
import getters from "./getters";

const initialState = {
  authenticating: false,
  user: null,
  funcionario: null,
};

if (isProduction) {
  initialState.user = window.PONTO.user;
}

export default {
  namespaced: true,
  state: initialState,
  modules: {
    acconts: require("./acconts").default
  },
  actions,
  mutations,
  getters
};
