<template>
  <div class="modal-backdrop" @click="closeModal">
      <div class="modal">
        <slot name="modal-header">
        </slot>
      <div class="bg-dark">234rsf</div>
        <slot name="body">
        </slot>

        <slot name="footer">
        </slot>
      </div>
    </div>
</template>

<script>
export default {
  name: 'ModalComponent',
  methods: {
    closeModal() {
      this.$emit('close');
    },
  },
};
</script>

<style scoped>


.modal1 {
  background: #FFBABA; /* или другой цвет */
  box-shadow: 2px 2px 20px 1px;
  overflow-x: hidden;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  max-width: 80%;
}


.modal-header,
.modal-footer {
  padding: 15px;
  display: flex;
}

.modal-header {
  border-bottom: 1px solid #eeeeee;
  color: #4AAE9B;
  justify-content: space-between;
}

.modal-footer {
  border-top: 1px solid #eeeeee;
  justify-content: flex-end;
}

.modal-body {
  position: relative;
  padding: 20px 10px;
}

.btn-close {
  border: none;
  font-size: 20px;
  padding: 20px;
  cursor: pointer;
  font-weight: bold;
  color: #4AAE9B;
  background: transparent;
}

</style>
