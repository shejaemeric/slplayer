import Vue from "vue";
import App from "./App.vue";
import router from "./router";

Vue.config.productionTip = false;
Vue.prototype.$playid = '0HqZX76SFLDz2aW8aiqi7G';
Vue.prototype.$playCover = '@/assets/others/main.jpg';

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
