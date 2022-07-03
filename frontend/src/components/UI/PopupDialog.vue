<template>
  <div class="dialog" v-if="show" @click="closeDialog">
    <div @click.stop class="dialog__content d-flex flex-column">
      <button
          class="btn_close"
          @click="closeDialog"
      >
        <img class="close" src="@/static/close.png" alt="">
      </button>
      <slot></slot>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    show: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    closeDialog() {
      this.$emit('updateShow', false)
    }
  },
  watch: {
    $route() {
      this.closeDialog()
    }
  }
}
</script>

<style scoped>
.dialog {
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  display: flex;
}

.dialog__content {
  overflow: scroll;
  margin: 30px auto auto auto;
  max-height: 90vh;
  background: #f1f0e8;
  border-radius: 12px;
  min-height: 50px;
  min-width: 300px;
  padding: 10px;
}

.close {
  width: 25px;
  border-style: none;
}

.btn_close {
  align-self: end;
  border-style: none;
  transition: all .6s;
}

.btn_close:hover {
  opacity: 0.7;
}
</style>