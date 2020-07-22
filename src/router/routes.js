import { requireUnauthenticated, requireAuthenticated } from "../modules/auth/guards";

export default [
        {
        path: "/login",
        name: "login",
        meta: {
            title: 'Login',
        },
        component: () =>
            import(/* webpackChunkName: "ponto_web" */ "../modules/auth/views/Login.vue"),
        beforeEnter: requireUnauthenticated
        },
        {
            path: '/cadastro',
            name: 'cadastro',
            meta: {
              title: 'Cadastro',
            },
            component: () => import(/* webpackChunkName: "ponto_web" */ "../modules/auth/views/Cadastro.vue"),
            beforeEnter: requireUnauthenticated,
        },
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
                    path: "config",
                    name: "config",
                    meta: {
                        title: "Config"
                    },
                    component: () => import(/* webpackChunkName: "ponto_web" */ "../components/Config.vue"),
                },
            ]
        }
]