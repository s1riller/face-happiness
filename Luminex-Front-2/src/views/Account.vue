<template>
  <body>

  <section class="page-header">
    <div class="container">
      <div class="row">
        <div class="col-md-12">

          <div class="content">
            <h1 class="page-name">С возвращением!</h1>
            <p>Мы рады видеть вас снова!</p>
          </div>
        </div>
      </div>
    </div>
  </section>
  <button @click="Logout" class="btn btn-success text-white rounded-5">Выйти</button>
  </body>
</template>

<script>
import axios from "axios";
import router from "@/router/router";

export default {
  name: 'AccountPage',

  data() {
    return {
      imageUrl: '',
    };
  },

  methods: {
    async Logout() {
      localStorage.removeItem('token');
      this.$router.push({ name: 'Home' });

      // Задержка в 1 секунду перед перезагрузкой страницы
      setTimeout(() => {
        location.reload();
      }, 1000);
    },

    async fetchRandomImage() {
      try {
        const accessKey = 'd8tTcQxso5iX38Zx_Hslrbi1uzkvOvDmtbS8OetWtdo';
        const response = await axios.get('https://api.unsplash.com/photos/random', {
          headers: {
            Authorization: `Client-ID ${accessKey}`,
          },
        });

        this.imageUrl = response.data.urls.regular;
      } catch (error) {
        console.error('Ошибка при запросе к Unsplash API:', error);
      }
    },
  },

  mounted() {
    // Вызов метода для получения случайного изображения при загрузке страницы
    this.fetchRandomImage();
  },
};
</script>
