<template>
  <select class="custom-select">
    <slot></slot>
  </select>
</template>

<script>
export default {
  name: "CustomSelect"
}
</script>

<style scoped>
.custom-select {
  border-style: none;
  align-self: flex-end;
  width: 100%;

  background-color: #cecbb7;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 5px;
}
select {
  padding: 0 6px;
}
</style>