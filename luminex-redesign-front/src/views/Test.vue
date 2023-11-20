<template>
  <button @click="openModal">Открыть модальное окно</button>
  <div class="modal" :class="{ 'show': showModal }">
    <div class="modal-dialog">
      <div class="modal-content">
        <!-- Контент модального окна -->
        <div class="modal-header">
          <h5 class="modal-title">Модальное окно</h5>
          <button type="button" class="close" @click="closeModal">
            <span>&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <!-- Содержимое модального окна -->
          <p>Привет, это модальное окно!</p>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

export default {
  name: 'TestPage',
  data() {
    return {
      showModal: false
    }
  },
  methods: {
    openModal: function () {
      this.showModal = true;
    },
    closeModal: function () {
      this.showModal = false;
    }
  }
};
</script>

<style scoped>


</style>
