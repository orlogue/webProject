<template>
  <button class="red-button">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "RedButton"
}
</script>

<style scoped>
.red-button {
  border-style: none;
  border-radius: 5px;
  background-color: #ea866b;
  transition: all .1s;
  padding: 3px 12px;
}

.red-button:active {
  background-color: #b25941;
}

</style>