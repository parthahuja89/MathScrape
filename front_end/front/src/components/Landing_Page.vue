<!-- Main Landing page for the website --> 
<template> 
<div>
<div id='heading'>   
MathScrape
</div>   
<div id= 'sub_heading'>
An intuitive Calculus Calculator, Scraper, 
and Grapher.     
</div> 
<div id = 'buttons'>
<b-button  id='landing_button_1' variant="info" @click ="routeToScraper"> Scraper</b-button>
<b-button  id='landing_button_2' variant="info" @click ="routeToCalculator"> Calculator</b-button>
</div> 
   <div id = 'usage'> Image by Francesco Ungaro </div> 
</div>
</template>
<!-- light scripts --> 
<script>
export default{
   data(){
      return{};
   },
   methods: {
      routeToScraper(){
         console.log("Routing to Scraper!")
         //router 
         this.$router.push({
                 path: '/home',
         });
      },
      routeToCalculator(){
         this.$router.push({
                 path: '/calculator',
         });
      }
   },
};
</script>

<style lang='scss'>
@import '../assets/css/landing_style.css'
</style>