import Vue from 'vue'
import App from './App'
import router from './router'
import VueProgressBar from 'vue-progressbar'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

const options = {
  color: '#6699ff',
  failedColor: '#99004d',
  thickness: '4px',
  transition: {
    speed: '0.2s',
    opacity: '0.6s',
    termination: 400
  },
  autoRevert: true,
  location: 'top',
  inverse: false
}

Vue.use(BootstrapVue)
Vue.use(VueProgressBar, options)


Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,

  components: { App },
  template: '<App/>'
})
