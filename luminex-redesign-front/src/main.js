import { createApp } from 'vue'
import App from './App.vue'
import router from "@/router"
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import Store from "@/store";

const app = createApp(App);

app.use(router)
app.use(Store)
// Vue.use(VModal, { dynamic: true });

app.mount('#app');

