<template>
    <Container :sidebar-items="sidebar" class="ponto-web" >
        <router-view />
    </Container>
</template>

<script>
import Container from "../modules/dashboard/containers/Container";

export default {
    components: {
        Container
        },
        data: () => ({
            sidebar: [
                {
                    text: "Home",
                    url : "home",
                    icon: "house-door"
                },
                {
                    text: "Ponto",
                    url : "ponto",
                    icon: "stopwatch"
                },
                {
                    text: "Configurações",
                    url : "config",
                    icon: "gear"
                }
            ]
        }),
    }
</script>

<style lang="scss">


</style>