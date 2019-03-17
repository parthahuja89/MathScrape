<template> 
<div>
  <div id="app">
       
       <router-view/>
       </div>
       </div>
  </template>
<script>
export default {
  created() {
   this.$Progress.start()
  },
  mounted(){
    this.$Progress.finish()
   },

  name: 'App' ,
}
</script>
