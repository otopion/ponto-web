<template>
    <div>
        <div class="config">
            <h2>Ponto</h2>
        </div>
        <div class="erro" v-if="dia.value===''">
            {{ dia.invalidFeedback }}
        </div>
        <div class="erro" v-if="dia.value!==''">
            {{ hora_chegada.invalidFeedback }}
        </div>
        <div class="lupa">
            <b-icon icon="search"/>
        </div>
        <div class="pesquisa">
            <ponto-date-picker v-model="pesquisa"/>
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
                            <th scope="col">Saida para almoço</th>
                            <th scope="col">Entrada do almoço</th>
                            <th scope="col">Presente</th>
                            <th scope="col">Opções</th>
                        </tr>
                        </thead>
                        <thead>
                        <tr>
                            <td>
                                <ponto-date-picker v-model="dia.value" disabled/>
                            </td>
                            <td>
                                <ponto-time-picker ref="date" v-model="hora_chegada.value"/>
                            </td>
                            <td>
                                <ponto-time-picker v-model="hora_saida"/>
                            </td>
                            <td>
                                <ponto-time-picker v-model="saida_almoco"/>
                            </td>
                            <td>
                                <ponto-time-picker v-model="entra_almoco"/>
                            </td>
                            <td>
                                <b-form-checkbox id="check" type="checkbox" v-model="falta"/>
                            </td>
                            <th>
                                <b-button id="button" type="submit" variant="outline-primary">Enviar</b-button>
                            </th>
                        </tr>
                        </thead>
                        <get-turno/>
                    </table>
                </b-form>
            </main>
            <edit-ponto/>
        </div>
    </div>
</template>

<script>
    import PontoDatePicker from "./PontoDatePicker";
    import PontoTimePicker from "./PontoTimePicker";
    import GetTurno from "./GetTurno";
    import EditPonto from "./EditPonto";

    export default {
        name: "Ponto",
        components: {
            EditPonto,
            GetTurno,
            PontoDatePicker,
            PontoTimePicker,
        },
        computed: {
            funcionario() {
                return this.$store.state.auth.funcionario;
            },
            pesquisa: {
                set(value) {
                    this.$store.dispatch("ponto/setPesquisa", value);
                }
            },
            turno() {
                 return this.$store.state.ponto.turno.slice().reverse();
            },
            hour: {
                set(value) {
                    this.$store.dispatch("ponto/setHour", value);
                },
            }
        },
        data() {
            return {
                dia: {
                    state: null,
                    value: "",
                    invalidFeedback: ""
                },
                hora_chegada: {
                    state: null,
                    value: "",
                    invalidFeedback: ""
                },
                hora_saida: "",
                saida_almoco: "",
                entra_almoco: "",
                falta: false,
            }
        },
        mounted() {

        },
        methods: {
            async onSubmit() {
                this.dia.invalidFeedback = "";
                this.dia.state = null;
                this.hora_chegada.invalidFeedback = "";
                this.hora_chegada.state = null;

                const data = {
                    data: this.dia.value,
                    hora_chegada: this.hora_chegada.value.HH + ":" + this.hora_chegada.value.mm,
                    hora_saida: this.hora_saida.HH + ":" + this.hora_saida.mm,
                    saida_almoco: this.saida_almoco.HH + ":" + this.saida_almoco.mm,
                    entrada_almoco: this.entra_almoco.HH + ":" + this.entra_almoco.mm,
                    presente: this.falta,
                    id_funcionario: this.funcionario[0].id
                };

                try {
                    await this.$store.dispatch("ponto/postTurno", data);
                    alert("inserido com sucesso!");
                    this.$store.dispatch("ponto/getTurno");
                } catch ({response}) {
                    if (response.status === 400) {

                        if (this.dia.value === "") {
                            this.dia.state = false;
                            this.dia.invalidFeedback = "informe a data de hoje";
                            this.PontoTimePicker.methods.clear()
                        }

                        if (this.hora_chegada.value.HH === "" || this.hora_chegada.value.mm === "") {
                            this.hora_chegada.state = false;
                            this.hora_chegada.invalidFeedback = "informe a hora de chegada";

                        }
                        if (this.hora_chegada.value === "") {
                            this.hora_chegada.state = false;
                            this.hora_chegada.invalidFeedback = "informe a hora de chegada";
                        }
                    }
                }
            }
        }
    }
</script>

<style lang="scss">
    #check {
        position: static;
        margin-left: 8px;
    }

    .erro {
        position: absolute;
        top: 100px;
        right: 500px;
        color: red;
    }

    .pesquisa {
        position: absolute;
        top: 95px;
        margin-left: 800px;
    }

    .lupa {
        position: absolute;
        top: 100px;
        margin-left: 770px;
    }
    body{
        background-color: #eeeeee;
    }
</style>
