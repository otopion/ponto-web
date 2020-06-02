<template>
    <vue-timepicker
            format="HH:mm"
            @input="onInput"
            class="time"
            auto-scroll
            manual-input
            ref="time"
    />
</template>

<script>
    import 'vue2-timepicker/dist/VueTimepicker.css'
    import VueTimepicker from 'vue2-timepicker'
    import ptBR from "vuejs-datepicker/dist/locale/translations/pt-BR";

    export default {
        computed: {
            language() {
                return ptBR;
            },
        },
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
        methods: {
        onInput(value) {
            this.$emit("input", value);
        },
        clear(){
            this.$emit('input')
        }
    }
    }
</script>

<style scoped>
    .time{
        width: 140px;
    }
</style>