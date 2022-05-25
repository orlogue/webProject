<template>
  <div class="navbar py-3 px-4">
    <div class="logo"><strong>Рынок</strong></div>
<!--    <div class="">-->
      <my-button
          @click="$router.push('/profile')"
          class="entrance"
      >Мой профиль
      </my-button>
      <my-button
          @click="showDialog"
          class="entrance1"
      ><img  class="image4" src="@/static/4.png">
      </my-button>
<!--    </div>-->
  </div>
  <router-view>
  </router-view>
  <my-window v-model:show="dialogVisible">
  </my-window>

</template>

<script>
import MyWindow from "@/components/UI/MyWindow";
import MyButton from "@/components/UI/MyButton";
import SecondButton from "@/components/UI/SecondButton";
export default {
  components: {MyButton, MyWindow, SecondButton},
  data(){
    return {
      dialogVisible: false,
    }
  },
  methods:{
    showDialog(){
      this.dialogVisible = true;
    }
  }
}
</script>

<style scoped>
.image4 {
  width: 30px;
  margin-top: 10px;
}
/*.entrance1 {*/
/*  margin-top: 90px;*/
/*}*/
.navbar {
  display: flex;
  flex-direction: row;
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