<template>
  <section class="products section">
    <div class="container">
      <div class="row">
        <div v-if="loading" class="text-center">
          <i class="fa fa-spinner fa-spin"></i> Загрузка продуктов...
        </div>
        <div  v-for="product in products" :key="product.id" class="col-md-4">
          <div class="product-item">
            <div class="product-thumb">
              <img class="img-responsive" :src="product.img" alt="product-img" />
              <div class="preview-meta">
                <ul>
                  <li @click="showProductModal(product)">
                    <span data-toggle="modal" data-target="#product-modal">
                      <i class="tf-ion-ios-search-strong"></i>
                    </span>
                  </li>
                  <li>
                    <a href="#" @click="addToFavorites(product)">
                      <i class="tf-ion-ios-heart"></i>
                    </a>
                  </li>
                  <li>
                    <a href="#" @click="addToCart(product)">
                      <i class="tf-ion-android-cart"></i>
                    </a>
                  </li>
                </ul>
              </div>
            </div>
            <div class="product-content">
              <h4><a href="#">{{ product.name }}</a></h4>
              <p class="price">${{ product.price }}</p>
            </div>
          </div>
        </div>

        <!-- ... другие элементы ... -->

        <!-- Modal.vue -->
        <div class="modal product-modal fade" id="product-modal">
          <!-- ... содержимое модального окна ... -->
        </div><!-- /.modal -->
      </div>
    </div>
  </section>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios';
export default {
  name: 'ShopPage',
  data() {
    return {
      products: [],
      loading: false,
    };
  },
  created() {
    this.fetchProducts(); // Добавьте эту строку
  },
  methods: {
    async fetchProducts() {
      try {
        this.loading = true; // Устанавливаем флаг загрузки в true перед запросом
        const response = await axios.get('http://127.0.0.1:8000/api/medicines/');
        this.products = response.data;
      } catch (error) {
        console.error('Ошибка при получении списка продуктов:', error);
      } finally {
        this.loading = false; // Вне зависимости от результата запроса, устанавливаем флаг загрузки в false
      }
    },
 }
};
</script>
