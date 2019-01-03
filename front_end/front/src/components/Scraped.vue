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
         x^2 - 4 ac _
     </div>

     <div  id = 'sympy'>
     <!-- Handling sympy requests -->

     </div>
  </b-card>
  </div>
</template>
<script>
export default {
data(){
    return{
     loading: true,
     eqs: [],
     equation: ''
    }
},
created: () => {
       console.log('Completed Scraping...')
       console.log('Equation recieved :' , this.eqs)
    }
}
</script>
