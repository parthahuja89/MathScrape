import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Scraped from '@/components/Scraped'
Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home, 
    },

    {
     path: '/Scraped',
     name: 'Scraped',
     component: Scraped, 
    }
  ],

});
