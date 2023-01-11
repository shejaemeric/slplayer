import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css'
import vuetify from './plugins/vuetify'


Vue.config.productionTip = false;
Vue.prototype.$playid = '0HqZX76SFLDz2aW8aiqi7G';
Vue.prototype.$playCover = '@/assets/others/main.jpg';

new Vue({
  router,
  vuetify,
  render: (h) => h(App)
}).$mount("#app");

Vue.use(Vuetify);
