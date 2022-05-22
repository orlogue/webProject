<template>
  <body>
    <div class="navbar">
      <strong><div class="logo">Рынок</div></strong>
      <div class="btn">
      <my-button
          class="entrance"
          @click="showDialog"
      >Войти
      </my-button>
      <my-button
          class="entrance1"
          @click="showDialog1"
      >Регистрация
      </my-button>
      </div>
    </div>
    <img class="image1" src="@/static/1.png">
    <div class="base">
      Добро пожаловать <br>
      на Рынок
    </div>
    <div class="info">
      <img class="image3" src="@/static/3.png">
      <div class="base2">Эта платформа поможет вам<br>
        купить нужные товары<br>
        на кампусе ДВФУ</div>
    </div>
    <div class="footer">
      ©2022
    </div>

    <my-window v-model:show="dialogVisible">
        <au-form></au-form>
    </my-window>
    <my-window v-model:show="dialogVisible1">
        <re-form></re-form>
    </my-window>

  </body>
</template>

<script>
import MyButton from "@/components/UI/MyButton";
import MyWindow from "@/components/UI/MyWindow";
import AuForm from "@/components/AuForm";
import ReForm from "@/components/ReForm";
export default {
  components: {
    ReForm,
    AuForm,
    MyWindow, MyButton
  },
  data(){
    return {
      dialogVisible: false,
      dialogVisible1: false,
    }

  },
  methods: {
    showDialog(){
      this.dialogVisible = true;
    },
    showDialog1(){
      this.dialogVisible1 = true;
    },
  }

}
</script>

<style >
@import url('https://fonts.googleapis.com/css2?family=Ruda&display=swap');
body{
  background-image: url('@/static/2.jpg');
  margin: 0;
  padding: 0;
  font-family: 'Ruda', sans-serif;
  position: relative;
}
 .btn1 {
  font-size: 25px ;
  color: #3D405B;
}
.navbar {
  height: 50px;
  display: flex;
  align-items: center;
  margin: 30px;
}
.entrance {
  margin-left: auto;
  margin-bottom: 15px;
  font-size: 25px ;
  color: #3D405B;
}
.entrance1 {
  margin-left: auto;
  margin-bottom: 15px;
  font-size: 25px ;
  color: #3D405B;
}

.logo {
  font-size: 38px;
  color: #3D405B;
  margin-left: 10px;
}
.image1 {
  margin-top: 100px;
  margin-left: -168px;
  width: 1000px;
}
.base {
  font-size: 70px;
  position: absolute;
  margin-top: -400px;
  margin-left: 800px;
  color: #3D405B;

}
.btn {
  margin:  0 0 0  1050px;
}
.info {
  background: #81b29a; /* Цвет фона */
  box-shadow: 0 0 10px rgba(0,0,0,0.2); /* Параметры тени */
  padding: 100px 0 100px 100px;
  margin: 40px 200px 0 200px;
  border-radius: 20px;
}
.image3 {
  width: 450px;
}
.base2 {
  margin-left: 550px;
  margin-top: -300px;
  margin-bottom: 15px;
  font-size: 45px ;
  color: #3D405B;
}
.footer {
  background: #81b29a;
  margin-top: 120px;
  padding-left: 710px;
  padding-top: 20px;
  padding-bottom: 20px;
}
.window {

}
.window1 {

}
</style>