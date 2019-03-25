<template>
<div> 
<div>
<!-- Card container --> 
<b-card title="Calculator"
        img-alt="Image"
        img-top
        tag="article"
        class="mb-2">
<p class="card-text">
    </p>


    <b-form-input 
                v-model="equation"
                type="text"
                placeholder="Enter the equation"
                class='fields'></b-form-input>

<!-- Collapsible tabs --> 
  <div role="tablist">
    <!-- Tab 1 --> 
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block href="#" v-b-toggle.accordion1 variant="info">Algebra</b-button>
      </b-card-header>
      <b-collapse id="accordion1" visible accordion="my-accordion" role="tabpanel">
        <b-card-body>
           <b-button  class = 'calculate_button' variant="light" @click ="Simplify"> Simplify Expression </b-button> 
            <b-button  class = 'calculate_button' variant="light" @click ="rationalize"> Rationalize </b-button> 
            <b-button  class = 'calculate_button' variant="light" @click ="evaluate"> Trig Value ( Ex. cos(45 deg) )</b-button> 
            <b-button  class = 'calculate_button' variant="light" @click ="sqrt"> sqrt </b-button> 

        </b-card-body>
      </b-collapse>
    </b-card>

    <!-- Tab 2 -->
    <b-card no-body class="mb-1">
      <b-card-header header-tag="header" class="p-1" role="tab">
        <b-button block href="#" v-b-toggle.accordion2 variant="info">Calculus</b-button>
      </b-card-header>
      <b-collapse id="accordion2" accordion="my-accordion" role="tabpanel">
        <b-card-body>
            <b-button  class = 'calculate_button' variant="light" @click ="evaluate"> Evaluate </b-button> 
            <b-button  class = 'calculate_button' variant="light" @click ="derivative"> Derivative ( ∂y / ∂x)</b-button> 
            <b-button  class = 'calculate_button' variant="light" @click ="integral"> Indefinite Integral ( ∫ ∂x )</b-button> 
        </b-card-body>
      </b-collapse>
    </b-card>
    <!-- Todo: Add graphing functionality-->
  </div>
</b-card>
</div>
</div>
</template>


<script> 
import * as math from 'mathjs';
math.import(require('mathjs-simple-integral'));
export default {
  data() {
      return{
          equation: ''
     };
  },
  methods:{
      runMethod(){
          console.log(math.sqrt(-4))
          this.equation = math.sqrt(-4).toString()
      },
      
      Simplify(){
          console.log('User equation: ', this.equation)
          this.equation = math.simplify(this.equation).toString()
      },
      rationalize(){
          console.log('User equation: ', this.equation)
          this.equation = math.rationalize(this.equation).toString()
      },
      evaluate(){
          console.log('User equation: ', this.equation)
          this.equation = math.eval(this.equation).toString()          
      },
      sqrt(){
          console.log('User equation: ', this.equation)
          this.equation = math.sqrt(this.equation).toString() 
      },
      derivative(){
          console.log('User equation: ', this.equation)
          this.equation = math.derivative(this.equation, 'x').toString() 
      },
      integral(){
          console.log('User equation: ', this.equation)
          this.equation = math.integral(this.equation, 'x').toString() 
      }
  },
};
</script>
<style lang='scss'>
@import '../assets/css/calculator.css'
</style>