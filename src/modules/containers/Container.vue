<template>
<div class="cont">
        <div>
            <Header />
        </div>
        <div>
            <sidebar :items="sidebarItems" />
        </div>
        <div class="slot">
            <slot />
        </div>
    </div>
</template>

<script>
    import Sidebar from "../Sidebar";
    import Header from "../Header";

    export default {
        name: "Container",
        components: {
            Header,
            Sidebar,
        },
         props: {
             sidebarItems: {
                 required: true,
                 type: Array
             }
         }
    }
</script>

<style lang="scss">
.slot {
        margin-left: 270px;
        margin-top: 90px;
        margin-right: 20px;
    }
    body{
        background-color: #eeeeee;
    }
</style>