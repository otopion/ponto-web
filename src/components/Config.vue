<template>
    <div>
        <div class="config">
            <h2>Configurações</h2>
        </div>

        <main class="tabela container view-home-container p-4 card shadow-sm my-3">
            <table class="table">
      <thead class="thead-light">
        <tr>
          <th scope="col">Nome</th>
          <th scope="col">Sobre nome</th>
          <th scope="col">Email</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row"><span>{{ user.first_name }}</span></th>
          <td><span >{{ user.last_name }}</span></td>
          <td><span >{{ user.email }}</span></td>
        </tr>
      </tbody>

    </table>
      <table class="table">
       <thead class="thead-light">
        <tr>
          <th scope="col">Hora de chegada</th>
          <th scope="col">Hora de saida</th>
        </tr>
      </thead>
          <tbody>
        <tr>
          <th><span>{{ funcionario[0].hora_chegada }}</span></th>
          <td><span >{{ funcionario[0].hora_saida }}</span></td>
        </tr>
      </tbody>
           <div class="alterar">
                <a href="" id="senha">Trocar senha</a>
               <a href="">Alterar horario</a>
           </div>
       </table>
        </main>
    </div>
</template>

<script>
export default {
    name: "Config",
    computed: {
        user() {
            return this.$store.state.auth.user;
        },
        funcionario() {
            return this.$store.state.auth.funcionario;
        },
        fun() {
            return this.$store.getters["auth/fun"];
        }

    },
}

</script>

<style lang="scss">
    .info{
        margin-top: 50px;
    }
    .alterar{
        margin-top: 150px;
    }
    #senha{
        margin-right: 20px;
    }
</style>