<template>
  <body class="w-100 vh-100 bg-discord-black">



  <div class="bd-masthead mb-3" id="content">
    <div class="container-xxl bd-gutter">
      <div class="col-md-8 mx-auto text-center">
<!--        <svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" fill="currentColor" class="bi bi-tencent-qq text-white pt-5" viewBox="0 0 16 16">-->
<!--          <path d="M6.048 3.323c.022.277-.13.523-.338.55-.21.026-.397-.176-.419-.453-.022-.277.13-.523.338-.55.21-.026.397.176.42.453Zm2.265-.24c-.603-.146-.894.256-.936.333-.027.048-.008.117.037.15.045.035.092.025.119-.003.361-.39.751-.172.829-.129l.011.007c.053.024.147.028.193-.098.023.063.017-.11-.006-.142-.016-.023-.089-.08-.247-.118Z"/>-->
<!--          <path d="M11.727 6.719c0-.022.01-.375.01-.557 0-3.07-1.45-6.156-5.015-6.156-3.564 0-5.014 3.086-5.014 6.156 0 .182.10-.535.10-.557l-.72 1.795a25.85 25.85 0 0 0-.534 1.508c-.68 2.187-.46 3.093-.292 3.113.36.044 1.401-1.647 1.401-1.647 0 .979.504 2.256 1.594 3.179-.408.126-.907.319-1.228.556-.29.213-.253.43-.201.518.228.386 3.92.246 4.985.126 1.065.12 4.756.26 4.984-.126.052-.088.088-.305-.2-.518-.322-.237-.822-.43-1.23-.557 1.09-.922 1.594-2.2 1.594-3.178 0 0 1.041 1.69 1.401 1.647.168-.02.388-.926-.292-3.113a25.78 25.78 0 0 0-.534-1.508l-.72-1.795ZM9.773 5.53a.095.095 0 0 1-.009.096c-.109.159-1.554.943-3.033.943h-.017c-1.48 0-2.925-.784-3.034-.943a.098.098 0 0 1-.018-.055c0-.015.004-.028.01-.04.13-.287 1.43-.606 3.042-.606h.017c1.611 0 2.912.319 3.042.605Zm-4.32-.989c-.483.022-.896-.529-.922-1.229-.026-.7.344-1.286.828-1.308.483-.022.896.529.922 1.23.027.7-.344 1.286-.827 1.307Zm2.538 0c-.484-.022-.854-.607-.828-1.308.027-.7.44-1.25.923-1.23.483.023.853.608.827 1.309-.026.7-.439 1.251-.922 1.23ZM2.928 8.99c.213.042.426.081.639.117v2.336s1.104.222 2.21.068V9.363c.326.018.64.026.937.023h.017c1.117.013 2.474-.136 3.786-.396.097.622.151 1.386.097 2.284-.146 2.45-1.6 3.99-3.846 4.012h-.091c-2.245-.023-3.7-1.562-3.846-4.011-.054-.9 0-1.663.097-2.285Z"/>-->
<!--        </svg>-->

        <h1 class="mb-3 fw-semibold lh-1 text-white pt-5">ПРЕДСТАВЬТЕ СЕБЕ…</h1>
        <p class="lead mb-4 text-white">
           место, где найдете уютное пространство, где каждый посетитель будет чувствовать себя как дома, независимо от цели посещения. Это место, где вы можете провести тест и получить рекомендации для ухода за вашей кожей лица. Здесь вы также можете обсудить результаты теста и поделиться своим опытом с друзьями и единомышленниками. Наш сайт создан для того, чтобы общение и обмен информацией о коже стали легкими и приятными.</p>
        <div v-if="token==='null'"  class="d-flex flex-column flex-lg-row align-items-md-stretch justify-content-md-center gap-3 mb-4">
          <button type="button" class="btn bg-light rounded-5" data-bs-toggle="modal" data-bs-target="#signupModal">
            Нужна учетная запись?
          </button>
          <button type="button" class="btn btn-outline-success me-2 rounded-5" data-bs-toggle="modal" data-bs-target="#signinModal">
            Получить результат
          </button>
        </div>

        <div v-if="token!=='null'"  class="d-flex flex-column flex-lg-row align-items-md-stretch justify-content-md-center gap-3 mb-4">
          <button @click.prevent="$router.push({ name: `Test` })" type="button" class="btn bg-light rounded-5">
           Пройти тест
          </button>
        </div>
<!--        this.$router.replace({ name: 'performance' });-->


      </div>
    </div>
  </div>

    <modal  v-if="showModal">
      sdd
    </modal>


  </body>
</template>
<style scoped>
html {
  overflow-x: hidden; /* Отключает горизонтальный скролл */
  overflow-y: hidden; /* Отключает вертикальный скролл */
}

.bg-discord-black{
  background-color: #23272A;
}
</style>
<script>

export default {
  data() {
    return {
      token: localStorage.getItem('token'),
      showModal: false,
    }
  },
  methods:{
    openModal() {

      console.log('sads')
      this.showModal = true;

    },

  }
}
</script>