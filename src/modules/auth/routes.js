import { requireUnauthenticated } from "./guards";
export default [
  {
    path: "/login",
    name: "login",
    component: () =>
      import(/* webpackChunkName: "login" */ "@/modules/auth/views/Login.vue"),
    beforeEnder: requireUnauthenticated,
  },
];