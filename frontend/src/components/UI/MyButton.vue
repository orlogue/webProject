<template>
  <button class="btns">
    <!--   все. что мы используем в май батн, будет
    уходить в этот слот  -->
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
  align-self: flex-end;
  background-color: #81b29a;
  transition: all .6s;
}
.btns:hover{
  opacity: 0.7;

}

</style>