import { requireAuthenticated } from "../modules/auth/guards";
import { routes as authRoutes, guards as authGuards } from "@/modules/auth";

export default [
        {
            path: "/login",
            name: "login",
            component: () =>
              import(/* webpackChunkName: "login" */ "@/modules/auth/views/Login.vue"),
            beforeEnter: authGuards.requireUnauthenticated,
        },
        {
            path: '/cadastro',
            name: 'cadastro',
            meta: {
                title: 'Cadastro'
            },
            component: () => import(/* webpackChunkName: "ponto_web" */ "../modules/auth/views/Cadastro.vue"),
            beforeEnter: authGuards.requireUnauthenticated,
        },
    ...authRoutes,
        {
            path: '/',
            name: 'pontoWeb',
            meta: {
                title: 'PontoWeb',
            },
            component: () => import(/* webpackChunkName: "ponto_web" */ "../views/PontoWeb.vue"),
            beforeEnter: requireAuthenticated,
            redirect: {
                name: "home"
            },
            children: [
                {
                    path: 'home',
                    name: 'home',
                    meta: {
                        title: "Home"
                    },
                    component: () => import(/* webpackChunkName: "ponto_web" */ "../components/Home.vue")
                },
                {
                    path: 'ponto',
                    name: 'ponto',
                    meta: {
                        title: "Ponto"
                    },
                    component: () => import(/* webpackChunkName: "ponto_web" */ "../components/Ponto.vue"),
                },
                {
                    path: "/config",
                    name: "configuracao",
                    component: () =>
                      import("../components/Config.vue"),
                    beforeEnter: requireAuthenticated

                },
            ]
        }
]