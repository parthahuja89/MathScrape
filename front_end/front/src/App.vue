<template>

  <div id="app">
       <vue-progress-bar></vue-progress-bar>
        <b-nav>
    <b-nav-item active>Active</b-nav-item>
    <b-nav-item>Link</b-nav-item>
    <b-nav-item>Another Link</b-nav-item>
    <b-nav-item disabled>Disabled</b-nav-item>
     </b-nav>
       <router-view/>
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

<style lang='scss'>
@import 'assets/css/style.css'
</style>
