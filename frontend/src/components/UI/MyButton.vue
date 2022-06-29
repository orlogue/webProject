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
  align-self: flex-end;
  background-color: #81b29a;
  transition: all .3s;
}
/*.btns:hover{*/
/*  opacity: 0.7;*/

/*}*/
.btns:active, :hover {
  color: #0b182c;
}

</style>