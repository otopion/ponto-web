<template>
    <div class="fundo">
        <br>
        <label><h3>Ponto Web</h3></label>
        <b-form>
            <div class="formulario"><b-form-input v-model="login.email" placeholder="Email" /></div>
            <div class="formulario"><b-form-input type="password" v-model="login.senha" placeholder="Senha"/></div>
            <div id="check"><b-checkbox v-model="login.manter" > Lembrar-me</b-checkbox></div>
            <b-button id="botao" href="/home">Entrar</b-button>
        </b-form>
    </div>
</template>

<script>
    export default {
        name: "Login",

        data(){
            return{
                logins:[], login:{}
            }
        }
    }
</script>

<style lang="scss">
    .fundo{
        width: 500px;
        min-height: 560px;
        position: relative;
        margin-top: 40px;
        margin-left: 450px;
        text-align: center;
        background-color: #00aeef;
        border-radius: 10px;
    }
    .formulario{
        width: 350px;
        margin-left: 85px;
        margin-top: 50px;
    }
    #botao{
        width: 350px;
        margin-top: 40px;
        margin-left: 20px;

    }
    #check{
        float: right;
        margin-top: 30px;
        margin-right: 305px;
    }
    body{
        background-color: #eeeeee;
    }
</style>