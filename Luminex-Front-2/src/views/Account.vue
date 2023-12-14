<template>
  <div class="container mt-3">
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
      <!-- User Test Results Section -->
      <div
          class="col"
          v-for="(result, index) in sortedUserTestResults"
          :key="index"
      >
        <div class="card shadow-sm">
          <div class="image-collage">
            <div
                v-for="(image, imageIndex) in parseMedicineImage(decodeUnicodeEscapes(result.medicine))"
                :key="imageIndex"
                class="image"
            >
              <img :src="image" :alt="'Image ' + (imageIndex + 1)">
            </div>
          </div>
          <div class="card-body">
            <p class="card-text">
              <ul>
                <li v-for="item in parseMedicineDescription(result.medicine)">{{ item }}</li>
              </ul>
            </p>
            <div class="d-flex justify-content-between align-items-center">
              <div class="btn-group">
                <button type="button" class="btn btn-sm btn-outline-secondary" @click="showModal(result)">Посмотреть</button>
              </div>
              <small class="text-body-tertiary">{{ index === 0 ? 'Последнее тестирование' : '' }}</small>
            </div>

            <div class="ml-auto">
              <p>Оценка рекомендации</p>
              <Rating v-model="result.rate" :cancel="false" @click="updateRateOnServer(result.id,result.rate, $event)" />

            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal for Medicine Details -->
    <modal v-if="show" @close="closeModal">
      <template v-slot:header>
        <h2>Проанализировав ваши данные мы готовы предоставить лечение</h2>
      </template>
      <template v-slot:body>
        <h3>Рекомендуемые препараты:</h3>
        <h4>Количество:{{ selectedMedicines.length }}</h4>
        <div v-for="(medicine, index) in selectedMedicines" :key="index" class="medicine-item">
          <img :src="medicine.img" :alt="medicine.name" class="medicine-image">
          <div class="medicine-details">
            <h4>{{ medicine.name }}</h4>
            <p>{{ medicine.description }}</p>
          </div>
        </div>
      </template>
      <template v-slot:footer>
        <button @click="closeModal">Закрыть</button>
      </template>
    </modal>
  </div>

  <!-- Page Header Section -->
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

</template>

<script>
import { mapGetters,mapMutations } from 'vuex';
import axios from 'axios';
import Modal from "@/components/Modal.vue";
import StarRating from "@/components/StarRating.vue";
import Rating from 'primevue/rating';

export default {
  name: 'CombinedPage',
  components: {
    StarRating,
    Modal,
    Rating,
  },
  data() {
    return {
      show: false,
      selectedMedicines: [],
      imageUrl: '',
      value: null,
      ratings: [],
    };
  },

  computed: {
    ...mapGetters(['getUserTestResults']),

    sortedUserTestResults() {
      return this.getUserTestResults.slice().sort(this.compareByIdDesc);
    },

  },
  created() {
    this.$store.dispatch('fetchUserTestResults');
  },
  methods: {
    setRateResult(resultIndex, rate) {
      this.$store.commit('setRateResult', { resultIndex, rate });
    },

    updateRateOnServer(resultId, rate) {
      this.$store.dispatch('updateRateOnServer', { resultId, rate });
    },
    getRate() {
      for (const el of this.sortedUserTestResults) {
        // Создаем объект с id и value
        const ratingObj = {
          id: el.id,
          value: el.rate,
        };
        // Добавляем объект в массив ratings
        this.ratings.push(ratingObj);
      }
    },
    async handleRatingSelected(result, rating, index) {
      // Отправить оценку на сервер для блока с индексом 'index'
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/rate_recomendation/', {
          testId: result.id,
          rating: this.ratings[result.id],
        }, {
          headers: {
            'Authorization': `Token ${localStorage.getItem('token')}`
          }
        });
        // Обновить оценку в массиве 'ratings'
        this.$set(this.ratings, index, rating);
        this.ratings[result.id] = rating
        // Handle the server response, e.g., show a success message
        console.log('Rating sent successfully:', response.data);
      } catch (error) {
        console.error('Error sending rating:', error);
      }
    },
    showModal(result) {
      this.selectedMedicines = JSON.parse(this.decodeUnicodeEscapes(result.medicine));
      this.show = true; // Показать модальное окно
    },
    closeModal() {
      this.show = false; // Закрыть модальное окно
    },
    decodeUnicodeEscapes(text) {
      return text.replace(/\\u[\dA-Fa-f]{4}/g, function(match) {
        return String.fromCharCode(parseInt(match.substr(2), 16));
      });
    },
    getRandomItemsFromArray(array, count) {
      const shuffledArray = array.slice().sort(() => 0.5 - Math.random());
      return shuffledArray.slice(0, count);
    },
    parseMedicineDescription(medicine) {
      try {
        const parsedMedicine = JSON.parse(this.decodeUnicodeEscapes(medicine));
        return this.getRandomItemsFromArray(parsedMedicine.map(medicine => medicine.description), 3);
      } catch (error) {
        return ["Данные в обработке"]; // Или другое сообщение об ошибке
      }
    },
    parseMedicineImage(medicine) {
      try {
        const parsedMedicine = JSON.parse(this.decodeUnicodeEscapes(medicine));
        return this.getRandomItemsFromArray(parsedMedicine.map(medicine => medicine.img), 6);
      } catch (error) {
        return []; // Или другое сообщение об ошибке
      }
    },
    compareByIdDesc(a, b) {
      return b.id - a.id;
    },
    async Logout() {
      localStorage.removeItem('token');
      this.$router.push({ name: 'Home' });
      setTimeout(() => {
        location.reload();
      }, 1000);
    },
    async fetchRandomImage() {
      // Code to fetch a random image
    },
  },
  mounted() {
    this.fetchRandomImage();
    this.getRate();
  },
};
</script>
<style>
</style>
