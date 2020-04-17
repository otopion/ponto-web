<template>
    <div>
        <div class="config">
            <h2>Ponto</h2>
        </div>
        <div class="fundo">
            <main class="tabela container view-home-container p-4 card shadow-sm my-3">
                <table class="table">
                    <thead class="thead-dark">
                    <tr>
                        <th scope="col">Data</th>
                        <th scope="col">Horario de cegada</th>
                        <th scope="col">Horario de Saida</th>
                        <th scope="col">Saida para o almoço</th>
                        <th scope="col">Entrada do almoço</th>
                        <th scope="col">Falta</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <th scope="row"><ponto-date-picker  /></th>
                        <td><ponto-time-picker /></td>
                        <td><ponto-time-picker /></td>
                        <td><ponto-time-picker /></td>
                        <td><ponto-time-picker /></td>
                        <td><input type="checkbox" /></td>
                    </tr>
                    </tbody>
                </table>
            </main>
        </div>
    </div>
</template>

<script>
    import PontoDatePicker from "./PontoDatePicker";
    import PontoTimePicker from "./PontoTimePicker";

    export default {
        name: "Ponto",
        components: {
            PontoDatePicker,
            PontoTimePicker
        },
        props: {
            value: {
                type: String,
                required: true
            }
        },
    }
</script>

<style scoped>

</style>