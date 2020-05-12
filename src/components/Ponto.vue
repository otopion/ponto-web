<template>
    <div>
        <div class="config">
            <h2>Ponto</h2>
        </div>
        <div class="erro" v-if="dia.value===''">
            {{ dia.invalidFeedback }}
        </div>
        <div class="erro" v-if="dia.value!==''">
            {{ chegada.invalidFeedback }}
        </div>
        <div class="fundo">

            <main class="tabela container view-home-container p-4 card shadow-sm my-3">
                <b-form @submit.prevent="onSubmit">
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
                    <thead>
                    <tr>
                        <td>
                        <ponto-date-picker v-model="dia.value" />
                        </td>
                        <td><ponto-time-picker v-model="chegada.value"/></td>
                        <td><ponto-time-picker v-model="saida"/></td>
                        <td><ponto-time-picker v-model="saida_almoco"/></td>
                        <td><ponto-time-picker v-model="entra_almoco"/></td>
                        <td><b-form-checkbox type="checkbox" v-model="falta" /></td>
                        <th>
                            <b-button id="button" type="submit" variant="outline-primary">Enviar</b-button>
                        </th>
                    </tr>
                    </thead>
                    <get-turno />
                </table>
            </b-form>
            </main>
        </div>
    </div>
</template>

<script>
    import PontoDatePicker from "./PontoDatePicker";
    import PontoTimePicker from "./PontoTimePicker";
    import GetTurno from "./GetTurno";

    export default {
        name: "Ponto",
        components: {
            GetTurno,
            PontoDatePicker,
            PontoTimePicker
        },
        computed:{
            funcionario() {
                return this.$store.state.auth.funcionario;
            },
        },
        data(){
            return {
                dia: {
                    state: null,
                    value: "",
                    invalidFeedback: ""
                },
                chegada: {
                    state: null,
                    value: "",
                    invalidFeedback: ""
                },
                saida: "",
                saida_almoco: "",
                entra_almoco: "",
                falta: false,
                form: null,
            }
        },
        methods:{
            async onSubmit() {
                this.dia.invalidFeedback = "";
                this.dia.state = null;
                this.chegada.invalidFeedback = "";
                this.chegada.state = null;

                const data = {
                    dia: this.dia.value,
                    chegada: this.chegada.value.HH+":"+this.chegada.value.mm,
                    saida: this.saida.HH+":"+this.saida.mm,
                    saida_almoco: this.saida_almoco.HH+":"+this.saida_almoco.mm,
                    entra_almoco: this.entra_almoco.HH+":"+this.entra_almoco.mm,
                    falta: this.falta,
                    funcionario: this.funcionario[0].id
                };


                try {
                    await this.$store.dispatch("ponto/postTurno", data);
                    alert("inserido com sucesso!");
                }
                catch ({ response }) {
                if (response.status === 400) {

                    if(this.dia.value == ""){
                        this.dia.state = false;
                        this.dia.invalidFeedback = "informe a data de hoje";
                    }

                    if(this.chegada.value == ""){
                        this.chegada.state = false;
                        this.chegada.invalidFeedback = "informe a hora de chegada";
                    }
                }
                }
            }
        }
    }
</script>

<style lang="scss">
    #dbutton{
        width: 0px;
        margin-top: 2px;
    }
    #button{
        margin-top: 1px;
    }
    .erro{
        position: absolute;
        top: 100px;
        right: 500px;
        color: red;
    }

</style>
