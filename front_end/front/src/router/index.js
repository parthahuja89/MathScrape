/* eslint-disable */
import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Scraped from '@/components/Scraped'
import Landing_Page from '@/components/Landing_Page'
import Calculator from '@/components/Calculator'
Vue.use(Router)
export default new Router({
  routes: [
    {
      path: '/home',
      name: 'Home',
      component: Home, 
    },

    {
     path: '/Scraped',
     name: 'Scraped',
     component: Scraped, 
    },
    {
      path: '/',
      name: 'Scraped',
      component : Scraped,
    },
    {
      path:'/calculator',
      name: 'Calculator',
      component: Calculator
    }
  ],

});
