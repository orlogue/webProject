<template>
  <button class="btns1">
    <!--   все. что мы используем в май батн, будет
    уходить в этот слот  -->
    <slot></slot>
  </button>
</template>

<script>
export default {
}
</script>

<style scoped>
.btns1 {
  border-style: none;
  align-self: flex-end;
  background-color: #81b29a;
  transition: all .9s;
}
.btns1:hover{
  color: #E07A5F;

}

</style>