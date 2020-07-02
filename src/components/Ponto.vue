<template>
    <div>
        <div class="config">
            <h2>Ponto</h2>
        </div>
        <div class="erro" v-if="data.value===''">
            {{ data.invalidFeedback }}
        </div>
        <div class="erro" v-if="data.value!==''">
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
                                <ponto-date-picker v-model="data.value" />
                            </td>
                            <td>
                                <ponto-time-picker v-model="hora_chegada.value" :disabled="disabled"/>
                            </td>
                            <td>
                                <ponto-time-picker v-model="hora_saida" :disabled="disabled"/>
                            </td>
                            <td>
                                <ponto-time-picker v-model="saida_almoco" :disabled="disabled"/>
                            </td>
                            <td>
                                <ponto-time-picker v-model="entrada_almoco" :disabled="disabled"/>
                            </td>
                            <td>
                                <b-form-checkbox @change="check" id="check" type="checkbox" v-model="presente"/>
                            </td>
                            <th>
                                <b-button id="button" type="submit" variant="outline-primary">Enviar</b-button>
                            </th>
                        </tr>
                        </thead>
                        <get-turno/>
                    </table>
                </b-form>
                {{ hora_saida }}
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
                },
                get() {
                    return this.$store.state.ponto.pesquisa;
                },
            },
            turno() {
                 return this.$store.state.ponto.turno.slice().reverse();
            },
        },
        data() {
            return {
                data: {
                    state: null,
                    value: "",
                    invalidFeedback: ""
                },
                hora_chegada: {
                    state: null,
                    value: "",
                    invalidFeedback: "",
                },
                hora_saida: "",
                saida_almoco: "",
                entrada_almoco: "",
                presente: false,
                disabled: true
            }
        },
        methods: {
            async check() {
                this.disabled = this.presente;
                if (this.disabled) {
                    await this.limpaCampos();
                    this.limpaDados();
                }
            },
            limpaCampos(){
                this.hora_chegada.value = "HH:mm";
                this.hora_saida = "HH:mm";
                this.saida_almoco = "HH:mm";
                this.entrada_almoco  = "HH:mm";
            },
            limpaDados(){
                this.data.value = "";
                this.hora_chegada.value = "";
                this.hora_saida = null;
                this.saida_almoco = null;
                this.entrada_almoco  = null;
            },
            async onSubmit() {
                this.data.invalidFeedback = "";
                this.data.state = null;
                this.hora_chegada.invalidFeedback = "";
                this.hora_chegada.state = null;

                if(this.hora_chegada.value==="")
                    this.hora_chegada.value=null;
                if(this.hora_saida==="")
                    this.hora_saida=null;
                if(this.entrada_almoco==="")
                    this.entrada_almoco=null;
                if(this.saida_almoco==="")
                    this.saida_almoco=null;

                const data = {
                    data: this.data.value,
                    hora_chegada: this.hora_chegada.value,
                    hora_saida: this.hora_saida,
                    saida_almoco: this.saida_almoco,
                    entrada_almoco: this.entrada_almoco,
                    presente: this.presente,
                    id_funcionario: this.funcionario[0].id
                };

                try {
                    await this.$store.dispatch("ponto/postTurno", data);
                    alert("inserido com sucesso!");
                    await this.limpaCampos();
                    this.limpaDados();
                    await this.$store.dispatch("ponto/getTurno");
                } catch ({response}) {
                    if (response.status === 400) {
                        const { data } = response;

                        if (this.data.value === "") {
                            this.data.state = false;
                            this.data.invalidFeedback = "informe a data de hoje";
                        }
                        if (!this.hora_chegada.value && this.presente) {
                            this.hora_chegada.state = false;
                            this.hora_chegada.invalidFeedback = data.presente[0];
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
        margin-left: 780px;
    }

    .lupa {
        position: absolute;
        top: 100px;
        margin-left: 750px;
    }
    body{
        background-color: #eeeeee;
    }
</style>
