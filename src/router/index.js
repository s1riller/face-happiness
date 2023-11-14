import { createRouter, createWebHistory } from "vue-router";

import Home from "@/views/Home.vue"
import Cart from "@/views/Cart.vue";

const routes = [
    { path: "/", component: Home, name: 'Home' },
    { path: "/Cart", component: Cart, name: 'Cart' },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
