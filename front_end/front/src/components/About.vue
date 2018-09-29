<template> 
 <div>
     About the page 
      {{title}} <br />
       <button v-on:click= "getMessage">  Get data</button>
     </div>

</template>
<script> 
import axios from 'axios';
export default{ 
    name: 'About',
    data() {
        return {
            title: '' ,
            api: 'http://localhost:5000/'
        };
    },
    methods: {
         getMessage(event){
             //flask server 
             const path = this.api+ 'fuck'
             axios.get(path).then((mes) => {
             this.title = mes.data;
             }).catch((error) =>{
                 console.log(error);
             });
         },
         },
         created(){
           
         },
};
</script>