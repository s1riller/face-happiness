<template>

  <div>
    <Navbar/>
    <div class="app">
      <router-view></router-view>
    </div>
    <FooTer/>

  </div>
</template>
<script>


import "@/static/css/style.css";
import Navbar from "@/components/Navbar.vue";
import "@/static/plugins/themefisher-font/style.css";
import "@/static/plugins/animate/animate.css";
import "@/static/plugins/slick/slick.css";
import "@/static/plugins/slick/slick-theme.css";
import FooTer from "@/components/Footer.vue";
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"

export default {
  name: "App",
  components: {
    FooTer,
    Navbar,
  },
};
</script>

<style>
/* Ваш стиль, если необходимо добавить */
</style>
