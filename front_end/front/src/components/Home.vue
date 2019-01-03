<!-- Copyright 2018, Parth Ahuja, All rights reserved -->

/* eslint-disable */
<template>
<div>
  <!-- Layout -->
   <b-card title="Math Scrape"
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 22rem;"
          class="mb-2">
    <p class="card-text">
     MathJax Equation Scraping
      </p>


     <b-form-input v-if= "active"
                  v-model="url_native"
                  type="text"
                  placeholder="Enter the url"
                  class='fields'></b-form-input>


     <b-form-input v-if= "active"
                  v-model="tag"
                  type="text"
                  placeholder="Enter the tag to scrape"
                  class='fields'></b-form-input>



     <b-form-input v-if= "active"
                  v-model="css"
                  type="text"
                  placeholder="Enter the css selector"
                  id = 'css_field'
                  class='fields'
                  ></b-form-input>





    <b-button  variant="primary" @click ="sendURL"> Scrape</b-button>

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
     <b-alert variant="danger"
          dismissible
          :show="showDismissibleAlert"
          @dismissed="showDismissibleAlert=false"
          height="4px"
          class = "alert"
          >
   Accept terms of service to continue
 </b-alert>
  </div>

</template>

<script>
import axios from 'axios';
export default {
  data() {
      return{
      showDismissibleAlert : false,
       status: 'not_accepted',
       url_native: '' ,
       //'https://mathscrape.herokuapp.com/'
       api: 'https://mathscrape.herokuapp.com/',
       tag: '',
       css: '',
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
           tag: this.tag,
           css_selector: this.css
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
        this.showDismissibleAlert = true
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
