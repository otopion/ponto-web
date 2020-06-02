<template>
    <div>
        <div class="bg-modal" id="modall">
            <div  class="modall">
                <span class="close" @click="fechar()">&times;</span>
                <div id="textEdit">
                    <h4>Editar dados</h4>
                </div>
                <form @submit.prevent="editar">
                 <table class="table">
                    <thead class="thead-dark">
                    <tr>
                        <th scope="col">Data</th>
                        <th scope="col">Horario de cegada</th>
                        <th scope="col">Horario de Saida</th>
                        <th scope="col">Saida para o almoço</th>
                        <th scope="col">Entrada do almoço</th>
                        <th scope="col">Falta</th>
                        <th scope="col">Opções</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td><ponto-date-picker v-model="editData" /> </td>
                        <td><ponto-time-picker v-model="editChegada"/> </td>
                        <td><ponto-time-picker v-model="editSaida"/></td>
                        <td><ponto-time-picker v-model="editSaida_almoco" /></td>
                        <td><ponto-time-picker v-model="editEntrada_almoco"/></td>
                        <td><b-form-checkbox type="checkbox" v-model="editPresente" /></td>
                        <th>
                            <b-button id="button" @click="fechar()" type="submit" variant="outline-primary">Editar</b-button>
                        </th>
                    </tr>
                    </tbody>
                 </table>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import PontoDatePicker from "./PontoDatePicker";
    import PontoTimePicker from "./PontoTimePicker";

    export default {
        name: "EditPonto",
        components:{
            PontoDatePicker,
            PontoTimePicker
        },
        data(){
          return{
              editData: "",
              editChegada: "",
              editSaida: "",
              editSaida_almoco: "",
              editEntrada_almoco: "",
              editPresente: false,
          }
        },
        computed: {
            edit: {
                get() {
                    return this.$store.state.ponto.edit;
                },
            },
        },
        methods:{
            fechar(){
                document.getElementById('modall').style.top = "-100%";
            },
            async editar() {
                const data = {
                    data: this.editData,
                    hora_chegada: this.editChegada.HH + ":" + this.editChegada.mm,
                    hora_saida: this.editSaida.HH + ":" + this.editSaida.mm,
                    saida_almoco: this.editSaida_almoco.HH + ":" + this.editSaida_almoco.mm,
                    entrada_almoco: this.editEntrada_almoco.HH + ":" + this.editEntrada_almoco.mm,
                    presente: this.editPresente,
                    id_funcionario: this.edit.id_Funcionario,
                    id: this.edit.id,
                };

                try {
                    if (confirm("os dados serão editados")) {
                        await this.$store.dispatch("ponto/editTurno", data);
                        this.$store.dispatch("ponto/getTurno");
                    }
                } catch (e) {
                    console.error("outer", e.message);
                }
            }
        }
    }
</script>

<style lang="scss">
    .bg-modal{
        margin-top: 80px;
        width: 78%;
        height: 80%;
        background: rgba(0,0,0,0.75);
        position: fixed;
        z-index: 2;
        top: -200%;
        display: block;
        transition: 350ms;
    }
    .modall{

        border: 1px solid #000;
        border-radius: 5px;
        margin: 100px auto 0 auto;
        background-color: #fff;
    }
    .close{
        float: right;
        font-size: 30px;
        color: #000;
        transition: 350ms;
        cursor: pointer;
        width: 4px;
        margin-right: 20px;
    }
    .modall span:hover{
        color: #990000;
        transition: 350ms;
    }
    #textEdit{
        margin-left: 40%;
    }
</style>