<template>
<div class="center font-weight-bold">
    <div class="name">
        <h2><span v-if="isAuthenticated">{{ user.first_name }}</span></h2>
    </div>
    <div class="data">
        <h3 >{{ data }}</h3>
    </div>
    <div class="hora">
        <h4>{{ hora }}</h4>
    </div>
</div>
</template>

<script>
export default {
  name: "Home",
    data(){
      return{
          hora: "",
          data: ""
      }
    },
    methods:{
      showTime(){
          let dayName = new Array ("domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado")
          let monName = new Array ("janeiro", "fevereiro", "março", "abril", "Maio", "junho", "agosto", "outubro", "novembro", "dezembro")

          this.hora = ((new Date).toLocaleString().substr(11, 8,));
          let date = new Date();
          this.data = dayName[date.getDay() ]+", "+date.getDate()+" de "+monName[date.getMonth()]+" de "+date.getFullYear();
      },
    },
    mounted() {
      setInterval(() => {
            this.hora = ((new Date).toLocaleString().substr(11, 8,));
        }, 1000);
        this.showTime();
    },

        computed: {
            user() {
                return this.$store.state.auth.user;
            },
            isAuthenticated() {
                return this.$store.getters["auth/isAuthenticated"];
            }
        }
}
</script>

<style scoped>
.center{
    margin-top: 150px;
    margin-left: 120px;
    margin-right: 200px;
    text-align: center;
}

.data{
    margin: 50px;
}
</style>
