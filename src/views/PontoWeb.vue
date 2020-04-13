<template>
    <Container :sidebar-items="sidebar" class="ponto-web" >
        <router-view />
    </Container>
</template>

<script>
import Container from "../modules/containers/Container";

export default {
    components: {
        Container
        },
        data: () => ({
            sidebar: [
                {
                    text: "Home",
                    url : "home",
                    icon: "ion-ios-home"
                },
                {
                    text: "Ponto",
                    url : "ponto",
                    icon: "ion-ios-time"
                },
                {
                    text: "Configurações",
                    url : "config",
                    icon: "ion-ios-settings"
                }
            ]
        })
    }
</script>

<style lang="scss">


</style>