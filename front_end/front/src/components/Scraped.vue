<!-- Copyright 2018, Parth Ahuja, All rights reserved --> 

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
       console.log('welcome to scraping')
       console.log('curren')
       console.log(this.eqs)
    } 
}
</script> 
