import { createRouter, createWebHistory } from "vue-router";

import Home from "@/views/Home.vue"
import Cart from "@/views/Cart.vue";
import Shop from "@/views/Shop.vue";
import Test from "@/views/Test.vue";
const routes = [
    { path: "/", component: Home, name: 'Home' },
    { path: "/Cart", component: Cart, name: 'Cart' },
    { path: "/Shop", component: Shop, name: 'Shop' },
    { path: "/Test", component: Test, name: 'Test' },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
