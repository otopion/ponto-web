<template>
    <vue-timepicker
            format="HH:mm"
            @input="onInput"
            class="time"
            auto-scroll
            :disabled="disabled"
            :value="value"
            manual-input
    />
</template>

<script>
    import 'vue2-timepicker/dist/VueTimepicker.css'
    import VueTimepicker from 'vue2-timepicker'
    import ptBR from "vuejs-datepicker/dist/locale/translations/pt-BR";
    import moment from 'moment';

    export default {
        name: "PontoTimePicker",
        components:{
            VueTimepicker
        },
        computed: {
            language() {
                return ptBR;
            },
        },
        props: {
            value: {
              required: true,
            },
            disabled: {
                type: Boolean,
                default: false
            },
        },
        methods: {
            onInput(value) {
                if (value) {
                    value = moment(value, 'HH:mm').format('HH:mm');
                } else {
                    value = "";
                }
                this.$emit("input", value);
            },
        }
    }
</script>

<style>
    .time{
        width: 140px;
    }
    .vue__time-picker .clear-btn{
        left: 130px;
    }
</style>