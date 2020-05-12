import {SET_DIA, SET_TURNO} from "./types";
import ponto from "../../api/ponto";
import { isProduction } from "@/utils";

export default {
    setDia({ commit }, data){
        commit(SET_DIA, data);
    },
    postTurno({ dia, chegada, saida, saida_almoco, entrada_almoco, presente, id_Funcionario }) {
            return ponto
                .postTurno(dia, chegada, saida, saida_almoco, entrada_almoco, presente, id_Funcionario)
    },
    init({ commit }){
        return new Promise(resolve => {
      if (isProduction) {
        resolve();
      } else {
        ponto
          .getTurno()
          .then(({ data }) => {
            commit(SET_TURNO, data);
          })
          .finally(() => {
            resolve();
          });
      }
    });
    }
}