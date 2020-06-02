<template>
    <date-pick
        @input="onInput"
        placeholder="Data"
        format="dd/MM/yyyy"
        :language="language"
        clear-button-icon
        clear-button
        bootstrap-styling
        ref="myDatepicker"
        v-model="value"
    />
</template>

<script>
import DatePick from "vuejs-datepicker/dist/vuejs-datepicker";
import ptBR from "vuejs-datepicker/dist/locale/translations/pt-BR";
import formatISO from "date-fns/formatISO";

export default {
    name: "PontoDatePicker",
    components: {
        DatePick
    },
    props: {
        value: {
            type: String,
            required: true,
        },
    },
    computed: {
        language() {
            return ptBR;
        },
    },
    mounted() {
        this.now = new Date();
    },
    methods: {
        onInput(value) {
            if (value) {
                value = formatISO(value, { representation: "date" });
            } else {
                value = "";
            }
            this.$emit("input", value);
        }
    }
};
</script>