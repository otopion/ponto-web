<template>
    <div class="fundoo">
        <div id="login-form">
    <b-form @submit.prevent="onSubmit">
      <h1>Cadastrar</h1>
        <div class="row">
      <div class="col-lg-6">
          <b-form-group
              :invalid-feedback="username.invalidFeedback"
              :state="username.state"
          >
          <b-form-input placeholder="Nome de usuário"
               v-model="username.value"
               :state="username.state"
               @change="username.state = null" trim/>
          </b-form-group>
      </div>
        <div class="col-lg-6">
            <b-form-group
              :invalid-feedback="email.invalidFeedback"
              :state="email.state"
            >
          <b-form-input type="text" placeholder="Email"
               v-model="email.value"
               :state="email.state"
               @change="email.state = null" trim/>
          </b-form-group>
      </div>
        </div>

        <div class="row">
      <div class="col-lg-6">
          <b-form-group
              :invalid-feedback="first_name.invalidFeedback"
              :state="first_name.state"
            >
          <b-form-input type="text" placeholder="Nome"
               v-model="first_name.value"
               :state="first_name.state"
               @change="first_name.state = null" trim/>
          </b-form-group>
      </div>
        <div class="col-lg-6">
            <b-form-group
              :invalid-feedback="first_name.invalidFeedback"
              :state="first_name.state"
            >
          <b-form-input type="text" placeholder="Sobre nome"
               v-model="last_name.value"
               :state="last_name.state"
               @change="last_name.state = null" trim/>
            </b-form-group>
      </div>
        </div>

        <div>
            <b-form-group
              :invalid-feedback="password.invalidFeedback"
              :state="password.state"
            >
          <b-form-input type="password" placeholder="Senha"
               v-model="password.value"
               :state="password.state"
               @change="password.state = null" trim/>
            </b-form-group>
      </div>

        <div class="row">
      <div class="col-lg-6">
          <ponto-time-picker
            v-model="hora_chegada" />
          <label>Hora de entrada</label>
      </div>
        <div class="col-lg-6">
          <ponto-time-picker
            v-model="hora_saida"
             />
            <label>Hora de saída</label>
      </div>
            {{ erro }}
        </div>

      <b-button type="submit" class="login-btn">Cadastrar</b-button>

      <div class="bottom-links">
        <p>Já tem uma conta? faça o <a href="login">Login</a></p>
      </div>
  </b-form>
        </div>
    </div>
</template>

<script>

    import PontoTimePicker from "../../../components/PontoTimePicker";

    export default {
        name: "Cadastro",

        components:{
            PontoTimePicker
        },

        data(){
            return{
                username: {
                    state: null,
                    value: "",
                    invalidFeedback: ""
                },
                email:{
                    state: null,
                    value: "",
                    invalidFeedback: ""
                },
                first_name: {
                    state: null,
                    value: "",
                    invalidFeedback: ""
                },
                last_name: {
                    state: null,
                    value: "",
                    invalidFeedback: ""
                },
                password: {
                    state: null,
                    value: "",
                    invalidFeedback: ""
                },
                nonFieldErrorMessage: "",
                erro: "",
                user : 2,
            }
        },
        computed: {
            hora_chegada: {
                get() {
                    return this.$store.state.auth.acconts.hora_chegada;
                },
                set(value) {
                    this.$store.dispatch("auth/setChegada", value);
                }
            },
            hora_saida: {
                get() {
                    return this.$store.state.auth.acconts.hora_saida;
                },
                set(value) {
                    this.$store.dispatch("auth/setSaida", value);
                }
            },
        },
        mounted() {
            this.focusUsername();
        },
        methods:{
            focusUsername() {
            this.$refs.username.$el.focus();
        },
            async onSubmit() {
                this.nonFieldErrorMessage = "";
                this.username.state = null;
                this.username.invalidFeedback = "";
                this.email.state = null;
                this.email.invalidFeedback = "";
                this.first_name.state = null;
                this.first_name.invalidFeedback = "";
                this.last_name.state = null;
                this.last_name.invalidFeedback = "";
                this.password.state = null;
                this.password.invalidFeedback = "";
                this.erro = "";

                const data = {
                    username: this.username.value,
                    email: this.email.value,
                    first_name: this.first_name.value,
                    last_name: this.last_name.value,
                    password: this.password.value,
                };


                try {
                    await this.$store.dispatch("auth/cadastrar", data);
                    this.$router.push({
                        name: "login"
                    });

                }
                catch ({ response }) {
                if (response.status === 400) {
                    const { data } = response;

                    if (this.username.value.length < 4) {
                        this.username.state = false;
                        this.username.invalidFeedback = "Certifique-se de que este campo tenha mais de 4 caracteres."
                    }

                    if ("username" in data) {
                        this.username.state = false;
                        this.username.invalidFeedback = data.username[0];
                    }

                    if ("email" in data) {
                        this.email.state = false;
                        this.email.invalidFeedback = data.email[0];
                    }

                    if (this.email.value == "") {
                        this.email.state = false;
                        this.email.invalidFeedback = "Este campo não pode ser em branco.";
                    }

                    if (this.first_name.value == "") {
                        this.first_name.state = false;
                        this.first_name.invalidFeedback = "Este campo não pode ser em branco.";
                    }

                    if (this.last_name.value == "") {
                        this.last_name.state = false;
                        this.last_name.invalidFeedback = "Este campo não pode ser em branco.";
                    }

                    if ("password" in data) {
                        this.password.state = false;
                        this.password.invalidFeedback = data.password[0];
                    }

                    if ("non_field_errors" in data) {
                        this.nonFieldErrorMessage = data.non_field_errors[0];
                        this.password.value = "";
                    }

                    if(!this.hora_chegada){
                        this.erro = "preencha";
                    }
                    this.focusUsername();
                } else {
                    this.nonFieldErrorMessage =
                        "Erro desconhecido, tente novamente mais tarde.";
                }
            }
            }
        }
    }
</script>

<style lang="scss">
    #login-form input{
        margin-top:20px
    }

.fundoo{
        background-color: #00BCD4;
        min-height: 800px;
    }
    *{
    margin: 0;
    padding: 0;
    text-decoration: none;
    font-family: arial;
    box-sizing: border-box;
}
#login-form {
    width: 600px;
    background: #fff;
    padding: 80px 40px;
    border-radius: 20px;
    position: absolute;
    left: 50%;
    top: 380px;
    transform: translate(-50%,-50%);
    margin: 20px 0px;
}
#login-form h1 {
    text-align: center;
    color: #00bcd4;
    font-size: 30px;
}
#login-form p {
    font-size: 16px;
    color: #333;
}
#login-form p a {
    color: #00bcd4;
}
#login-form label {
    color: #848484;
}
.input-box{
    margin-right: 300px;
    position: relative;
    margin-top: 30px;
}
.input-box input{
    font-size: 15px;
    color: #333;
    border: none;
    width: 100%;
    outline: none;
    background: none;
    padding: 0 5px;
    height: 40px;
}
.input-box span::before{
    content: attr(data-placeholder);
    position: absolute;
    top: 50%;
    left: 5px;
    color: #adadad;
    transform: translateY(-50%);
    z-index: -1;
    transition: .5s;
}
.input-box span::after{
    content: '';
    position: absolute;
    width: 0%;
    height: 2px;
    background: linear-gradient(120deg,#2196F3,#FF5722);
    transition: .5s;
}
.focus + span::before{
    top: -5px;
}
.focus + span::after{
    width: 100%;
}
.login-btn {
    display: block;
    width: 100%;
    height: 50px;
    border: none;
    background: linear-gradient(70deg,#2196F3,#03bcd4,#2196F3);
    background-size: 200%;
    color: #fff;
    outline: none;
    cursor: pointer;
    margin: 20px 0px 0px;
    border-radius: 50px;
    transition: .5s;
    font-size: 18px;
    letter-spacing: 1px;
}
.login-btn:hover{
    background-position: right;
}
.bottom-links{
    margin-top: 30px;
    text-align: center;
    font-size: 13px;
}

@media (max-width: 575px){
#login-form {
    width: 300px;
}
}
</style>