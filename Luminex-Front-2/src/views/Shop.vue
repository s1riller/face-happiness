<template>
  <section class="products section">
    <div class="container">
      <div class="row">

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
export default {
  name: "ShopPage",
  data() {
    return {
      products: [],
    };
  },
  computed: {
    ...mapGetters(['getProductList']),
  },
  created() {

    this.products = this.getProductList;
  }
};
</script>
