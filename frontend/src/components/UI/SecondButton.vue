<template>
  <button class="btns1">
    <slot></slot>
  </button>
</template>

<script>
export default {}
</script>

<style scoped>
.btns1 {
  border-style: none;
  background-color: #81b29a;
  transition: all .3s;
}

.btns1:hover {
  color: #b94d31;
}

</style>