<template>
  <nav-bar></nav-bar>
<!--  <div class="container flex-fill">-->
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
    <div class="filter">
      Фильтрация
    </div>

    <div class="category">
      <div class="square1">
        Продукты
        <img class="ic1" src="@/static/icon1.png">
      </div>
      <div class="square1">
        Напитки
        <img class="ic1" src="@/static/icon2.png">
      </div>
      <div class="square1">
        Одежда
        <img class="ic1" src="@/static/icon3.png">
      </div>

      <div class="square1">
        Табачные изделия
        <img class="ic1" src="@/static/icon4.png">
      </div>
      <div class="square1">
        Другое
        <img class="ic1" src="@/static/icon5.png">
      </div>
    </div>
<!--  </div>-->

  <my-footer></my-footer>
</template>

<script>
import MyFooter from "@/components/UI/MyFooter";
import NavBar from "@/components/NavBar";
import SecondButton from "@/components/UI/SecondButton";
export default {
  components: {NavBar, MyFooter, SecondButton}
}
</script>

<style>

.square1 {
  background-color: #f4f1de;
  box-shadow: 0 0 10px rgba(0,0,0,0.2);
  border-radius: 10px;
  font-size: 20px;
  width: 190px;
  height: 190px;
  padding: 20px;
  margin-left: 70px;
  margin-bottom: 70px;
  transition: all .6s;
  text-align: center;
}
.square1:hover {
  box-shadow: 0 0 10px rgba(0,0,0,0.5);
}
.category {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  margin-left: 350px;
}
.item.new-string{
  width: 100%;
}
.ic1 {
  width: 150px;
}

.filter {
  margin: 20px;
  border-radius: 5px;
  background-color: #E07A5F;
  width: 235px;
  padding: 10px;
}
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

</style>