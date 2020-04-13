<template>
    <di>
        <div class="config">
            <h2>Configurações</h2>
        </div>

        <main class="tabela container view-home-container p-4 card shadow-sm my-3">
            <table class="table">
      <thead class="thead-light">
        <tr>
          <th scope="col">Nome</th>
          <th scope="col">Segundo Nome</th>
          <th scope="col">Email</th>
          <th scope="col">Senha</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th scope="row">Walison Vinicios</th>
          <td>Alves Ribeiro</td>
          <td>alves@simworx.com</td>
            <td>sim****</td>
        </tr>
      </tbody>
    </table>
            <div class="senha">
                <a href="login">Trocar senha</a>
            </div>
        </main>
    </di>
</template>

<script>
    export default {
        name: "Config"
    }
</script>

<style lang="scss">
    .info{
        margin-top: 50px;
    }
    .senha{
        margin-top: 200px;
    }
</style>