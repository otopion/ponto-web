import Vue from "vue";
import Vuex from "vuex";
import { store as auth } from "@/modules/auth";
import { isProduction } from "@/utils";
import createLogger from "vuex/dist/logger";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
  },
  strict: !isProduction,
  plugins: isProduction ? [] : [createLogger()]
});
