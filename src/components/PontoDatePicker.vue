<template>
    <date-pick
        @input="onInput"
        placeholder="Data"
        format="dd/MM/yyyy"
        :language="language"
        :value="dateValue"
        clear-button-icon
        clear-button
        bootstrap-styling
    />
</template>

<script>
import DatePick from "vuejs-datepicker/dist/vuejs-datepicker";
import ptBR from "vuejs-datepicker/dist/locale/translations/pt-BR";
import formatISO from "date-fns/formatISO";
import parseISO from "date-fns/parseISO";

export default {
    name: "PontoDatePicker",
    components: {
        DatePick
    },
    props: {
        value: {
            required: true,
        },
    },
    computed: {
        language() {
            return ptBR;
        },
        dateValue() {
            if (this.value === "") {
                return null;
            }
            return parseISO(this.value);
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