<template>

  <div id="app">
       <vue-progress-bar></vue-progress-bar>
       <b-navbar toggleable type="light" variant="light">
        <b-navbar-toggle target="nav_text_collapse"></b-navbar-toggle>
        <b-navbar-brand>MathScrape</b-navbar-brand>
        <b-collapse is-nav id="nav_text_collapse">
            <b-navbar-nav class="ml-auto">
                <b-nav-item> GitHub </b-nav-item>
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
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
