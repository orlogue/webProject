<template>
  <nav-bar>

  </nav-bar>
  <my-footer></my-footer>
</template>

<script>

import NavBar from "@/components/NavBar";
import MyFooter from "@/components/UI/MyFooter";
export default {
  components: { NavBar, MyFooter},
  data(){
    return {
      dialogVisible: true ,
    }
  },
  methods:{
    showDialog(){
      this.dialogVisible = true;
    }
  }
}
</script>

<style>


</style>