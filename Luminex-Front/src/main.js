import { createApp } from 'vue'
import App from './App'
// import components from '@/components/UI';
import router from "@/router/router";
import directives from '@/directives';
import store from '@/store/index';
import 'bootstrap'
// import './bootstrap/bootstrap.scss'
import 'bootstrap/dist/css/bootstrap.css';
import Vuex from 'vuex'
import components from '@/components/';
import Axios from 'axios'


const app = createApp(App)

components.forEach(component => {
  app.component(component.name, component)
})


directives.forEach(directive => {
  app.directive(directive.name, directive)
})


app.use(Vuex)
  .use(router)
  .use(store)
  .mount('#app');

