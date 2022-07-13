<template>
  <button class="btns">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: 'my-button'
}
</script>

<style scoped>
.btns {
  border-style: none;
  background-color: transparent;
  transition: all .3s;
}

.btns:active, :hover {
  color: #212529;
}

</style>