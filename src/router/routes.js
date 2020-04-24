import { requireAuthenticated } from "../modules/auth/guards";
import { routes as authRoutes, guards as authGuards } from "@/modules/auth";

export default [
    ...authRoutes,
        {
            path: '/',
            name: 'pontoWeb',
            meta: {
                title: 'PontoWeb',
                excludeBreadcrumb: true
            },
            component: () => import(/* webpackChunkName: "ponto_web" */ "../views/PontoWeb.vue"),
            beforeEnter: authGuards.requireAuthenticated,
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
                    component: () => import(/* webpackChunkName: "ponto_web" */ "../components/Ponto.vue")
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