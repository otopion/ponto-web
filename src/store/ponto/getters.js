export default {
  turno() {
    return this.$store.state.ponto.turno.slice().reverse();
  }
};