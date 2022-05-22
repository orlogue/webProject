<template>
  <input :value="modelValue" @input="updateInput" type="text" class="input">
</template>

<script>
export default {
  props: {
    modelValue:[String, Number]
  },
  methods: {
    updateInput(event){
      this.$emit('update:modelValue', event.target.value)
    }
    //  новое событие-первый параметр,значение,
    //  которое должно обновиться- второй

  }
}
</script>

<style>
.input {
  width: 100%;

  padding: 10px 15px;
  margin-top: 15px;
}
</style>