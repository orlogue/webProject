<template>
  <button class="green-button">
    <slot></slot>
  </button>
</template>

<script>
export default {
  name: "GreenButton"
}
</script>

<style scoped>
.green-button {
  border-style: none;
  border-radius: 5px;
  background-color: #81b29a;
  transition: all .1s;
  padding: 3px 12px;
}

.green-button:active {
  background-color: #608c76;
}

</style>