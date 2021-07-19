<template>
  <div class="container">
    <div class="row">
      <div v-if="this.questFinish == true">
        <h3 class="text-center">Resultado</h3>
            <div class="container my-5">
              <h4>Numeros inseridos: {{this.numbers}}</h4>
              <h4>Ordem inversa: {{this.inversa}}</h4>
              <h4>Soma: {{this.sum}}</h4>
              <h4>Média: {{this.media}}</h4>
              <h4>Valores superiores a média: {{this.acimaMedia}}</h4>
              <h4>Valores inferiores a 7: {{this.abaixo7}}</h4>
                <button type="button"
                  class="btn btn-primary
                  mt-5 mr-3 btn-lg"
                  v-on:click.stop.prevent = resetQuest
                  >Reiniciar</button>
            </div>
          </div>
      </div>
      <div v-if="this.questStart == true">
        <h1>Insira suas notas</h1>
        <hr>
      <div class="col-8">
         <b-form-group
            label="Insira Sua Nota e clique em Enviar ou adicione -1 como nota
            para executar as operações"
            label-for="input-formatter"
            description="(apenas numeros reais!)"
            class="mb-0"
          >
            <b-form-input
              id="addNota"
              v-model="number"
              placeholder=""
            ></b-form-input>
          </b-form-group>
              <div class="float-right">
                  <button type="button"
                  class="btn btn-success
                  mt-5 mr-3 btn-lg"
                  v-on:click.stop.prevent = addNotas
                  >adicionar Nova Nota</button>
                  <button type="reset"
                  class="btn btn-warning
                  mt-5 mr-2 btn-lg"
                  v-on:click.stop.prevent = postNumbers
                  >Enviar</button>
              </div>
            </div>
       </div>
      </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      numbers: [],
      number: null,
      result: [],
      inversa: [],
      sum: 0,
      media: 0,
      acimaMedia: 0,
      abaixo7: 0,
      questFinish: false,
      questStart: true,
    };
  },
  methods: {
    addNotas() {
      const num = parseInt(this.number, 10);
      if (Number.isNaN(num)) {
        window.alert('Insira um valor!');
      } else if (num < -1) {
        this.number = null;
        window.alert('Insira um valor positivo!');
      } else if (num === -1) {
        this.postNumbers();
      } else {
        this.numbers.push(num);
        this.number = null;
      }
    },
    postNumbers() {
      const path = 'http://localhost:5000/numbers';
      const payload = {
        numbers: this.numbers,
      };
      axios.post(path, payload)
        .then((res) => {
          this.result = res.data;
          this.inversa = res.data.inversa;
          this.sum = res.data.sum;
          this.media = res.data.media;
          this.acimaMedia = res.data.acimaMedia;
          this.abaixo7 = res.data.abaixo7;
          console.log('foi');
          this.questFinished();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log('numdeu');
          console.log(error);
        });
      this.finished = true;
    },
    questFinished() {
      this.questFinish = true;
      this.questStart = false;
    },
    resetQuest() {
      this.questFinish = false;
      this.questStart = true;
      this.reset();
    },
    reset() {
      this.finished = false;
      this.numbers = [];
      this.number = null;
    },
  },
};
</script>
