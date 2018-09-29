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
      Enter your URL 
      </p>
     
     <b-form-input v-model="url"
                  type="text"
                  placeholder="Enter your name"></b-form-input>
    <p>Value: {{ url }}</p>
    
    <b-button  variant="primary" @click ="sendURL">Go somewhere</b-button>

  </b-card>

  <b-form-checkbox id="checkbox1"
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
       url: '' ,
       api: 'http://localhost:5000/'
     };
  },
  methods: {
    sendURL(event){
      console.log('trying to connect to server');
      const path = this.api+ 'send_url'
      if(this.status == 'accepted'){
         //make axios promise 
         axios.post(path, {
           url: 'google.com',    
         })
         .then(function(response){
           console.log(response);
         })
         .catch(function(error){
           console.log(error);
           })
      }else{
        console.log('accept the service')
      }
    }
  },
 };
</script>  

