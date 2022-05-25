<template>
  <nav-bar></nav-bar>
<!--  <div class="d-flex flex-column">-->
    <div class="menu">
      <second-button
          class="btn_menu1"
          @click="$router.push('/category')"
      >
        Категории
      </second-button>
      <second-button
          class="btn_menu2"
          @click="$router.push('/product')"
      >
        Все товары
      </second-button>
    </div>

    <router-view>
    </router-view>
    <my-window v-model:show="dialogVisible">
    </my-window>

    <div class="filter">
      Фильтрация
    </div>
<!--  </div>-->
  <my-footer></my-footer>
</template>

<script>
import SecondButton from "@/components/UI/SecondButton";
import MyFooter from "@/components/UI/MyFooter";
import NavBar from "@/components/NavBar";
export default {
  components: { NavBar, MyFooter, SecondButton},
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
.menu {
  margin-top: 100px;
  margin-left: 20px;
  width: auto;
}
.btn_menu1 {
  font-size: 20px;
  background-color: #f4f1de;
  margin-right: 10px;
  margin-left: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.2);
  border-radius: 5px;
}
.btn_menu2 {
  font-size: 20px;
  background-color: #f4f1de;
  box-shadow: 0 0 10px rgba(0,0,0,0.2);
  border-radius: 5px;
}
.filter {
  margin: 20px;
  border-radius: 5px;
  background-color: #E07A5F;
  width: 235px;
  padding: 10px;
}


</style>