import { createRouter, createWebHistory } from "vue-router";

import Home from "@/pages/Home"
import Testing from "@/pages/TestingPage.vue"
import Performance from "@/pages/PerformancePage.vue"
import Statistics from "@/pages/ StatisticsPage.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/Testing", component: Testing },
  { path: "/Performance", component: Performance},
  { path: "/Statistic", component: Statistics},

];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
