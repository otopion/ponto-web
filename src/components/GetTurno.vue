<template>
    <tbody>
    <tr v-for="(item, i ) in filter" :key="i">
        <td v-if="item.id_Funcionario===funcionario[0].id">{{ item.data }}</td>
        <td v-if="item.id_Funcionario===funcionario[0].id">{{ item.hora_chegada }}</td>
        <td v-if="item.id_Funcionario===funcionario[0].id">{{ item.hora_saida }}</td>
        <td v-if="item.id_Funcionario===funcionario[0].id">{{ item.saida_almoco }}</td>
        <td v-if="item.id_Funcionario===funcionario[0].id">{{ item.entrada_almoco }}</td>
        <td v-if="item.id_Funcionario===funcionario[0].id">{{ item.presente }}</td>
        <td v-if="item.id_Funcionario===funcionario[0].id">
            <b-button class="op" @click="abrir(item)" variant="primary"><b-icon class="icon" icon="pencil-square"/> </b-button>
            <b-button @click="excluir(item.id)" class="op" variant="danger"><b-icon class="icon" icon="trash"/></b-button>
        </td>
    </tr>
    </tbody>
</template>

<script>

    import  'bootstrap-vue/dist/bootstrap-vue-icons.min.css';

    export default {
        name: "GetTurno",
        data(){
            return{
                item: [],
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
            this.$store.dispatch("ponto/getTurno");
            let i = 0;
            while(this.turno[i] != null) {
                this.turno[i].data = this.turno[i].data.split('-').reverse().join('/');
                i++;
            }
            let k = 0;
            while(this.turno[k] != null){
                if(this.turno[k].presente === true )
                    this.turno[k].presente = "Presente";

                if(this.turno[k].presente === false )
                    this.turno[k].presente = "Ausente";
                k++;
            }
        },
        methods:{
           excluir(id) {
                try {
                    this.delet = id;
                    if(confirm("Deseja mesmo excluir o item?")){
                        this.$store.dispatch("ponto/deleteTurno", this.delet);
                    }
                } catch (e) {
                     console.error("outer", e.message);
                }
            },
            abrir(item){
              document.getElementById('modall').style.top = "0";
              this.edit = item;
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
</style>