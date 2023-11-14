<template>
  <div>
    <Navbar></Navbar>
    <div class="app">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>


import "@/static/css/style.css";
import Navbar from "@/components/Navbar.vue";
import "@/static/plugins/themefisher-font/style.css";
import "@/static/plugins/animate/animate.css";
import "@/static/plugins/slick/slick.css";
import "@/static/plugins/slick/slick-theme.css";

export default {
  name: "App",
  components: {
    Navbar,
  },
};
</script>

<style>
/* Ваш стиль, если необходимо добавить */
</style>
