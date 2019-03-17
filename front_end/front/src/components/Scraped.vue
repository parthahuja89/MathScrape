<!-- Copyright 2018, Parth Ahuja, All rights reserved -->

<!-- Post Scraping page with results -->
/* eslint-disable */
<template>
    <div>
   <b-card title="Math Scrape"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem;"
          class="mb-2">
    <p class="card-text">
     mathjax webscraping
      </p>

     <div id='scraped_text'>

         Scraped equation:

     </div>
     <!-- populate this with the scraped equation NON PARSED VERSION ONLY --> 
      <b-form-textarea rows="3" v-model="text" max-rows="100" id='flood_eq'  placeholder="Scraped Equation" />
      <b-button id='parse_to_latex' variant="info" @click ="parseToLatex"> Parse to LATEX </b-button>
      
      <!-- Parsed Latex --> 
  <div id='katex_1'></div>
  </b-card>
  </div>
</template>
<script>
import axios from 'axios';
//changing jQuery --> jquery (Depracted)
import jQuery from 'jquery';
import katex from 'katex';
export default {
data(){
    return{
     text: '',
     loading: true,
     equation: '',
     eqs: Object,
    }
},
//Lesson learnt: Don't use arrows if you want access to 'this'
created:function() {
       console.log('Checking if query is passing: ', this.$route.params.eqs)
},
mounted:function(){
    console.log('Mounted...')
    console.log('Checking if query is passing: ', this.$route.params.eqs)
    jQuery('#flood_eq').val(this.$route.params.eqs["data"].slice(-1).pop())
     
},
methods:{
    parseToLatex(){
        //Rendering the latex text 
        console.log('Rendering LaTeX')
        katex.render(this.$route.params.eqs["data"].slice(-1).pop(), katex_1, {
            displayMode: true,
         });
    },
    routeToCalculator(){
    
    }
}
}
</script>
<style lang='scss'>
@import '../assets/css/style.css'
</style>
<style>
  @import "../../node_modules/katex/dist/katex.min.css";
</style> 
