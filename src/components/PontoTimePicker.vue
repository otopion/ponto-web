<template>
    <vue-timepicker
            format="HH:mm"
            @input="onInput"
            class="time"
    />
</template>

<script>
    import 'vue2-timepicker/dist/VueTimepicker.css'
    import VueTimepicker from 'vue2-timepicker'
    import ptBR from "vuejs-datepicker/dist/locale/translations/pt-BR";

    export default {
        name: "PontoTimePicker",
        components:{
            VueTimepicker
        },
        props: {
            value: {
                type: String,
                required: true
            }
        },
        computed: {
        language() {
            return ptBR;
        },
    },
        methods: {
        onInput(value) {
            this.$emit("input", value);
        }
    }
    }
</script>

<style scoped>
    .time{
        width: 150px;
    }
</style>