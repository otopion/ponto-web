import Vue from 'vue';
import App from './App.vue';
import { BootstrapVue } from "bootstrap-vue";
import { BootstrapVueIcons } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'bootstrap-vue/dist/bootstrap-vue-icons.min.css';

import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app');
