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
                    <thead class="thead-dark" id="text-edit">
                    <tr>
                        <th scope="col">Data</th>
                        <th scope="col">Horario de cegada</th>
                        <th scope="col">Horario de Saida</th>
                        <th scope="col">Saida para o almoço</th>
                        <th scope="col">Entrada do almoço</th>
                        <th scope="col">Presente</th>
                        <th scope="col">Opções</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr >
                        <td><ponto-date-picker  v-model="edit.data" /></td>
                        <td><ponto-time-picker v-model="edit.hora_chegada" :disabled="!edit.presente" /> </td>
                        <td><ponto-time-picker v-model="edit.hora_saida" :disabled="!edit.presente" /></td>
                        <td><ponto-time-picker v-model="edit.saida_almoco" :disabled="!edit.presente" /></td>
                        <td><ponto-time-picker v-model="edit.entrada_almoco" :disabled="!edit.presente" /></td>
                        <td><b-form-checkbox @change="check" type="checkbox" v-model="edit.presente" /></td>
                        <th>
                            <b-button id="buttonEdit"  type="submit" variant="outline-primary">Editar</b-button>
                        </th>
                    </tr>
                    </tbody>
                 </table>
                    <div class="editErro">
                        <div v-if="edit.data===''">
                            {{ erroData.invalidFeedback }}
                        </div>
                        <div v-if="edit.data!=='' && edit.hora_chegada===''">
                            {{ erroChegada.invalidFeedback }}
                        </div>
                    </div>
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
            PontoTimePicker,
        },
        data(){
          return{
              disabled: true,
              erroData: {
                  state: null,
                  invalidFeedback: "",
              },
              erroChegada: {
                  state: null,
                  invalidFeedback: "",
              },
          }
        },
        computed: {
            edit: {
                set(value) {
                    this.$store.dispatch("ponto/setEdit", value);
                },
                get() {
                    return this.$store.state.ponto.edit;
                },
            },
        },
        methods:{
            async check() {
                if (this.edit.presente) {
                    await this.limpaCampos();
                    this.limpaDados();
                }
            },
            limpaCampos(){
                this.$store.dispatch("ponto/limpaCamposEdit");
            },
            limpaDados(){
                this.$store.dispatch("ponto/limpaDadosEdit");
            },
            async fechar() {
                await this.limpaCampos();
                this.limpaDados();
                this.erroData.invalidFeedback = "";
                this.erroChegada.invalidFeedback = "";
                document.getElementById('modall').style.top = "-100%";
            },
            async editar() {
                this.erroData.invalidFeedback = "";
                this.erroData.state = null;
                this.erroChegada.invalidFeedback = "";
                this.erroChegada.state = null;

                const data = {
                    data: this.edit.data,
                    hora_chegada: this.edit.hora_chegada,
                    hora_saida: this.edit.hora_saida,
                    saida_almoco: this.edit.saida_almoco,
                    entrada_almoco: this.edit.entrada_almoco,
                    presente: this.edit.presente,
                    id_funcionario: this.edit.id_funcionario,
                    id: this.edit.id,
                };

                if(data.hora_chegada==="")
                    data.hora_chegada=null;
                if(data.hora_saida==="")
                    data.hora_saida=null;
                if(data.entrada_almoco==="")
                    data.entrada_almoco=null;
                if(data.saida_almoco==="")
                    data.saida_almoco=null;

                try {
                    if (confirm("os dados serão editados")) {
                        await this.$store.dispatch("ponto/editTurno", data);
                        await this.$store.dispatch("ponto/getTurno");
                        this.fechar();
                    }
                } catch ({response}) {
                    if (response.status === 400) {
                        const { data } = response;

                        if (this.edit.data === "") {
                            this.erroData.invalidFeedback = "informe a data de hoje";
                        }
                        if (!this.edit.hora_chegada && this.edit.presente) {
                            this.erroChegada.state = false;
                            this.erroChegada.invalidFeedback = data.presente[0];
                        }
                    }
                }
            },
        }
    }
</script>

<style lang="scss">
    #text-edit{
        font-size: 14px;
    }
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
    .editErro{
        margin-left: 40%;
        color: red;
    }
</style>