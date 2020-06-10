<template>
    <tbody>
    <tr v-for="(item, i ) in pageOfItems" :key="i">
        <td>{{ item.data }}</td>
        <td v-if="item.hora_chegada">{{ item.hora_chegada }}</td>
        <td v-else>{{ traco }}</td>
        <td v-if="item.hora_saida">{{ item.hora_saida }}</td>
        <td v-else>{{ traco }}</td>
        <td v-if="item.saida_almoco">{{ item.saida_almoco }}</td>
        <td v-else>{{ traco }}</td>
        <td v-if="item.entrada_almoco">{{ item.entrada_almoco }}</td>
        <td v-else>{{ traco }}</td>
        <td v-if="item.presente">{{ item.presente }}</td>
        <td>
            <b-button class="op" @click="abrir(item)" variant="primary"><b-icon class="icon" icon="pencil-square"/> </b-button>
            <b-button @click="excluir(item.id)" class="op" variant="danger"><b-icon class="icon" icon="trash"/></b-button>
        </td>
    </tr>
    <tr>
        <td colspan="7"><jw-pagination id="pagenation" :items="filter" @changePage="onChangePage" ></jw-pagination></td>
    </tr>
    </tbody>

</template>
<script>
    import  'bootstrap-vue/dist/bootstrap-vue-icons.min.css';
    import JwPagination from 'jw-vue-pagination';
    import { mapActions } from "vuex";

    export default {
        name: "GetTurno",
        components:{
          JwPagination,
        },
        data(){
            return{
                item: [],
                pageOfItems: [],
                traco: "- - - - - - - -"
            }
        },
        computed:{
            funcionario() {
                return this.$store.state.auth.funcionario;
            },
            turno() {
                 return this.$store.state.ponto.turno.slice().reverse();
            },
            delet:{
                set(value) {
                    this.$store.dispatch("ponto/setDelete", value);
                },
                get() {
                    return this.$store.state.ponto.delete;
                },

            },
            pesquisa:{
                get() {
                    return this.$store.state.ponto.pesquisa;
                },
            },
            edit:{
                set(value) {
                    this.$store.dispatch("ponto/setEdit", value);
                },
                get() {
                    return this.$store.state.ponto.edit;
                },
            },

            filter: function(){
                return this.turno.filter((item) =>{
                    return item.data.match(this.pesquisa.split('-').reverse().join('/'))
                })
            },
        },
        mounted() {

        },
        methods:{
            ...mapActions(["abrirEdit"]),

            onChangePage(pageOfItems) {
                this.pageOfItems = pageOfItems;
                window.scrollTo(0, 0);
            },
            async excluir(id) {
                try {
                    this.delet = id;
                    if(confirm("os dados seram excluidos")) {
                        await this.$store.dispatch("ponto/deleteTurno", this.delet);
                        await this.$store.dispatch("ponto/getTurno");
                    }
                } catch (e) {
                    console.error("outer", e.message);
                }
            },
            async abrir(item) {
                await this.$store.dispatch("ponto/abrirEdit", item);
                document.getElementById('modall').style.top = "0";
            },

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
    #pagenation{
        left: 25%;
        width: 550px;
        position: relative;
        margin-left: 100px;
    }
</style>