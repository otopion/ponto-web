<template>
    <tbody>
    <tr v-for="(item, i ) in turno" :key="i">
        <td v-if="item.id_Funcionario===funcionario[0].id">{{ item.data }}</td>
        <td v-if="item.id_Funcionario===funcionario[0].id">{{ item.hora_chegada }}</td>
        <td v-if="item.id_Funcionario===funcionario[0].id">{{ item.hora_saida }}</td>
        <td v-if="item.id_Funcionario===funcionario[0].id">{{ item.saida_almoco }}</td>
        <td v-if="item.id_Funcionario===funcionario[0].id">{{ item.entrada_almoco }}</td>
        <td v-if="item.id_Funcionario===funcionario[0].id">{{ item.presente }}</td>
        <td v-if="item.id_Funcionario===funcionario[0].id">
            <b-button class="op" variant="primary"><b-icon class="icon" icon="pencil-square"/> </b-button>
            <b-button class="op" variant="danger"><b-icon class="icon" icon="trash"/></b-button>

        </td>
    </tr>
    </tbody>
</template>

<script>
    import  'bootstrap-vue/dist/bootstrap-vue-icons.min.css'
    export default {
        name: "GetTurno",
        computed:{
            funcionario() {
                return this.$store.state.auth.funcionario;
            },
            turno() {
                return this.$store.state.auth.turno.slice().reverse();
            }
        },
    }
</script>

<style scoped>
    .op{
        width: 30px;
        height: 30px;
        text-align: center;
        float: left;
        top: 50%;
        position: relative;
        display: flex;
        justify-content: center;
        margin-right: 2px;
    }
    .icon{
        margin-left: 10px;
    }
</style>