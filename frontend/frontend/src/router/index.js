import Vue from "vue";
import VueRouter from "vue-router";
import SearchView from "../views/SearchView";
import AuthView from "../views/AuthView";
import HomeView from "../views/HomeView.vue"

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: SearchView,
  },
  {
    path: "/auth",
    name: "auth",
    component: AuthView,
  },
  {
    path:"/test",
    name:"test",
    component: HomeView,
  }
];

const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
