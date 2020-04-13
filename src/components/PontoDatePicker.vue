<template>
    <date-pick
        format="dd/MM/yyyy"
        :language="language"
        clear-button
        bootstrap-styling
    />
</template>

<script>
    import DatePick from "vuejs-datepicker/dist/vuejs-datepicker";
    export default {
        name: "DatePicker",
        components:{
            DatePick
        },
    }
</script>

<style scoped>

</style>