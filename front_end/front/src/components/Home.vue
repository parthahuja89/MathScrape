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
     
     <b-form-input v-if= "active"
                  v-model="url_native"
                  type="text"
                  placeholder="Enter the url"></b-form-input>
    <p>Value: {{ url_native }}</p>
    
    <b-button  variant="primary" @click ="sendURL">Go somewhere</b-button>

  </b-card>

  <b-form-checkbox   v-if= "active"
                     id="checkbox1"
                     v-model="status"
                     value="accepted"
                     unchecked-value="not_accepted">
      I accept the terms and use
    </b-form-checkbox>
    <div>State: <strong>
     
      {{status}}
       
     </strong></div>


  </div>
  
</template>

<script> 
import axios from 'axios';
export default {
  data() {
     return{
       status: 'not_accepted',
       url_native: '' ,
       api: 'http://localhost:5000/',
       active: true, 
     };
  },
  methods: {
    sendURL(event){
      //PROMISING 
      console.log('trying to connect to server');
      const path = this.api+ 'send_url'
      if(this.status == 'accepted'){
         //make axios promise 
         axios.post(path, {
           url: this.url_native,    
         })
         .then(function(response){
           console.log(response);
         })
         .catch(function(error){
           console.log(error);
           })
      }else{ //send warning 
        console.log('accept the service')
      }
       //route with recieved data 
    
      /*
       * routing to scraping page 
       */
       
  
     
    }  
  },
 };
</script>  

