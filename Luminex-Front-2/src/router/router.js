import { createRouter, createWebHistory } from "vue-router";

import Home from "@/pages/Home"
import Testing from "@/pages/TestingPage.vue"
import Performance from "@/pages/PerformancePage.vue"
import Statistics from "@/pages/ StatisticsPage.vue";
import Products from "@/pages/ProductsPage.vue";
import LoginAttent from "@/components/LoginAttent.vue";
import Shop from "@/views/Shop.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";
import Account from "@/views/Account.vue";
const routes = [
  { path: "/", component: Home, name:'Home' },
  { path: "/Test", component: Testing, name:'Test' },
  { path: "/Shop", component: Shop, name:'Shop' },
  { path: "/Statistic", component: Statistics},
  { path: '/Performance', component: Performance, name: 'performance' },
  { path: '/Products', component: Products, name: 'products' },
  { path: '/Login', component: Login, name: 'Login' },
  { path: '/Register', component: Register, name: 'Register' },
  { path: '/Account', component: Account, name: 'Account' },

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});



// router.beforeEach((to, from, next) => {
//   if (to.path !== '/' && localStorage.getItem('token') === 'null') {
//
//
//
//       Home.methods.openModal()
//
//
//
//     next('/');
//   } else {
//     next();
//   }
// });

export default router;
