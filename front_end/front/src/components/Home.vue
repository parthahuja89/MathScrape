<!-- Copyright 2018, Parth Ahuja, All rights reserved -->

/* eslint-disable */
<template>
<div>
  <!-- Layout -->
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
 <b-button  variant="primary" @click ="debug"> debugging </b-button>
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
       api: 'https://mathscrape-server.herokuapp.com/',
       active: true,
       server_response: [],
       forwarding: false
     };
  },
  methods: {
    sendURL(event){

      //PROMISING
      console.log('trying to connect to server');
      const path = this.api

      if(this.status == 'accepted'){
         //make axios promise
          const instance = axios.create({
           baseURL: this.api

          });
          //pre-request
          instance.interceptors.response.use(response => {
          this.$Progress.finish()
           console.log(response);
           this.$router.push({
                 path: '/scraped',
                 params: { eqs: response }
                 });
             return response
            })

          //post request
          instance.interceptors.request.use(config => {
          this.$Progress.start()
          return config
          })



          //requests
          instance.post( '/send_url', {
           url: this.url_native,
           })
           .then(function(response){

           })
         .catch(function(error){
           console.log(error);
           })
          /*
          * route with data
           */
      }else{ //send warning
        //To proceed accept Terms and Service.

      }

    },
    debug(){
      this.$router.push({
                 path: '/scraped',

                 });
    }
  },

 };
</script>
