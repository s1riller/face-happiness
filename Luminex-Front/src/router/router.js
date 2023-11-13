import { createRouter, createWebHistory } from "vue-router";

import Home from "@/pages/Home"
import Testing from "@/pages/TestingPage.vue"
import Performance from "@/pages/PerformancePage.vue"
import Statistics from "@/pages/ StatisticsPage.vue";
import Products from "@/pages/ProductsPage.vue";
import LoginAttent from "@/components/LoginAttent.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/Testing", component: Testing, name:'testing' },
  { path: "/Statistic", component: Statistics},
  { path: '/Performance', component: Performance, name: 'performance' },
  { path: '/Products', component: Products, name: 'products' },

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});



router.beforeEach((to, from, next) => {
  if (to.path !== '/' && localStorage.getItem('token') === 'null') {



      Home.methods.openModal()



    next('/');
  } else {
    next();
  }
});

export default router;
