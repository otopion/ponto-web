import Vue from 'vue';
import Router from 'vue-router'

Vue.use(Router);

export default new Router({
    routes: [
        {
            path: '/login',
            name: 'login',
            meta: {
                title: 'Login',
            },
            component: () => import(/* webpackChunkName: "ponto_web" */ "../components/Login.vue"),
        },
        {
            path: '/',
            name: 'pontoWeb',
            meta: {
                title: 'PontoWeb',
                excludeBreadcrumb: true
            },
            component: () => import(/* webpackChunkName: "ponto_web" */ "../views/PontoWeb.vue"),
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
                    path: 'config',
                    name: 'configuracoes',
                    meta: {
                        title: "Configurações"
                    },
                    component: () => import(/* webpackChunkName: "ponto_web" */ "../components/Config.vue")
                },
            ]
        }],
    mode: "history"
})