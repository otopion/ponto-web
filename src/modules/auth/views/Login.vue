<template>
    <div class="fundoo">
    <div id="login-form">
    <b-form @submit.prevent="onSubmit">
      <h1>Bem vindo ao PontoWeb</h1>
        <div class="mensagem">
            <b-alert
                    :show="!!nonFieldErrorMessage"
                    variant="danger"
            >
                {{ nonFieldErrorMessage }}
            </b-alert>
        </div>
      <div>
            <b-form-group
                    :invalid-feedback="username.invalidFeedback"
                    :state="username.state"
            >
                <b-form-input
                    v-model="username.value"
                    :state="username.state"
                    @change="username.state = null"
                    :disabled="authenticating" placeholder="Nome de usuário" trim />
                </b-form-group>
      </div>

      <div>
          <b-form-group
                    :invalid-feedback="password.invalidFeedback"
                    :state="password.state"
            >
                <b-form-input type="password" class="input-box"
                    v-model="password.value" placeholder="Senha"
                    :state="password.state"
                    @change="password.state = null"
                    :disabled="authenticating" trim
            />
                </b-form-group>
      </div>

      <label>
        <b-form-checkbox
                v-model="rememberMe"
                :value="true"
                :unchecked-value="false"
                class="mb-3"
                :disabled="authenticating"
        >
            Lembrar-me
        </b-form-checkbox>
      </label>

      <b-button class="login-btn" type="submit">
          <template v-if="authenticating">
              <b-spinner small type="grow" class="mr-1" />
              <span>Aguarde...</span>
          </template>
            Entrar
      </b-button>

      <div class="bottom-links">
        <p>Você não tem uma conta? <a href="cadastro">Cadastrar</a></p>
      </div>
    </b-form>
    </div>
    </div>
</template>

<script>
    export default {
        name: "Login",

        data() {
        return {
            username: {
                state: null,
                value: "",
                invalidFeedback: ""
            },
            password: {
                state: null,
                value: "",
                invalidFeedback: ""
            },
            rememberMe: false,
            nonFieldErrorMessage: ""
        };
    },
        mounted() {
        this.focusUsername();
        },
        computed: {
            authenticating() {
                return this.$store.state.auth.authenticating;
            },
            isAuthenticated() {
                return this.$store.getters["auth/isAuthenticated"];
            }
        },

        methods:{
            focusUsername() {
            this.$refs.username.$el.focus();
        },
            async onSubmit() {
                this.nonFieldErrorMessage = "";
                this.username.state = null;
                this.username.invalidFeedback = "";
                this.password.state = null;
                this.password.invalidFeedback = "";

                const data = {
                    username: this.username.value,
                    password: this.password.value,
                    rememberMe: this.rememberMe
                };

                try {
                    await this.$store.dispatch("auth/login", data);
                    this.$router.push({
                        name: "home"
                    });
                }
                catch ({ response }) {
                if (response.status === 400) {
                    const { data } = response;
                    if ("username" in data) {
                        this.username.state = false;
                        this.username.invalidFeedback = data.username[0];
                    }

                    if ("password" in data) {
                        this.password.state = false;
                        this.password.invalidFeedback = data.password[0];
                    }

                    if ("non_field_errors" in data) {
                        this.nonFieldErrorMessage = data.non_field_errors[0];
                        this.password.value = "";
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
    .fundoo{
        height: 100%;
        background-color: #00BCD4;
        min-height: 680px;
    }
    .mensagem{
        font-size: 16px;
        min-height: 60px;
    }

    *{
    margin: 0;
    padding: 0;
    text-decoration: none;
    font-family: arial;
    box-sizing: border-box;
}
#login-form {
    width: 450px;
    background: #fff;
    padding: 80px 40px;
    border-radius: 20px;
    position: absolute;
    left: 50%;
    top: 50%;
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