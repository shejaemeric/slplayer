import Vue from "vue";
import VueRouter from "vue-router";
import SearchView from "../views/SearchView";
import AuthView from "../views/AuthView";

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
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
