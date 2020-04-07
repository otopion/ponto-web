<template>
<b-navbar class="navbar navbar-expand-lg navbar-light bg-light" fixed="top" id="fixed">
    <label class="navbar-brand">Ponto Web</label>
  <div class="collapse navbar-collapse" id="navbarNavDropdown" >
    <b-navbar-nav class="ml-auto">
            <slot name="nav-right" />
            <b-nav-item-dropdown class="nav-item dropdown m-2" right>

                <template v-slot:button-content>
                    <span>User</span>
                </template>

                <b-dropdown-item>Sair</b-dropdown-item>

            </b-nav-item-dropdown>
        </b-navbar-nav>
  </div>
</b-navbar>
</template>

<script>
    export default {
        name: "Header",
    }
</script>

<style scoped>
.navbar.type{
    background-color: #00aeef;
}
</style>