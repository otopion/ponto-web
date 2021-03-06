import store from "@/store";

export const requireAuthenticated = (to, from, next) => {
  store.dispatch("auth/init").then(() => {
    if (!store.getters["auth/isAuthenticated"]) {
      next({
        name: "login"
      });
    } else {
      store.dispatch("ponto/getTurno");
      store.dispatch("auth/getFuncionario");
      next();
    }
  });
};

export const requireUnauthenticated = (to, from, next) => {
  store.dispatch("auth/init").then(() => {
    if (store.getters["auth/isAuthenticated"]) {
      next({
        name: "home"
      });
    } else {
      next();
    }
  });
};
