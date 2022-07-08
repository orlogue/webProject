<template>
  <div class="navbar py-3 px-4">
    <div class="logo"><strong>FEFU market</strong></div>
    <div>
      <my-button
          v-if="!this.$store.state.isAuthenticated"
          class="nav-button"
          @click="showloginDialog"
      >Войти
      </my-button>
      <my-button
          v-if="!this.$store.state.isAuthenticated"
          class="nav-button"
          @click="showsignupDialog"
      >Регистрация
      </my-button>
      <my-button
          v-else
          class="nav-button"
          @click="this.$router.push('/products')"
      >Перейти в магазин
      </my-button>
    </div>
  </div>
  <div class="container">
    <div class="welcome">
      <img class="image1" src="@/static/1.png" alt="">
      <div class="base">
        Добро пожаловать <br>
        на FEFU market!
      </div>
    </div>
    <div class="info">
      <img class="image3" src="@/static/3.png" alt="">
      <div class="base2">
        <p class="title">Надоело чекать беседы при поиске товаров?</p>
        <p class="text">У нас ты можешь разместить товары на продажу
          или же купить у других людей на кампусе ДВФУ</p>
      </div>
    </div>
  </div>
  <my-footer></my-footer>

  <popup-dialog :show="loginVisible"
                @updateShow="closeDialog">
    <au-form></au-form>
  </popup-dialog>
  <popup-dialog :show="signupVisible"
                @updateShow="closeDialog">
    <re-form></re-form>
  </popup-dialog>
</template>

<script>
import MyButton from "@/components/UI/MyButton";
import PopupDialog from "@/components/UI/PopupDialog";
import AuForm from "@/components/AuForm";
import ReForm from "@/components/ReForm";
import MyFooter from "@/components/UI/MyFooter";

export default {
  components: {
    ReForm,
    AuForm,
    PopupDialog,
    MyButton,
    MyFooter
  },
  data() {
    return {
      loginVisible: false,
      signupVisible: false,
    }
  },
  methods: {
    showloginDialog() {
      this.loginVisible = true;
      document.querySelector('body').style.overflow = 'hidden'
    },
    showsignupDialog() {
      this.signupVisible = true;
      document.querySelector('body').style.overflow = 'hidden'
    },
    closeDialog() {
      this.loginVisible = false;
      this.signupVisible = false;
      document.querySelector('body').removeAttribute('style')
    }
  }

}
</script>

<style>
.btn1 {
  font-size: 25px;
  color: #3D405B;
}

.btn_aut {
  background-color: #81b29a;
  font-size: 20px;
  padding: 5px 13px;
  border-radius: 4px;
  border: 1px;
  color: #f4f1de;
  transition: all .4s;
}

.btn_aut:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.4);
}

.welcome {
  display: flex;
  align-items: center;
  margin: 50px 0 0 0;
}

.image1 {
  margin-left: -210px;
  width: 1000px;
}

.base {
  font-size: 70px;
  line-height: 95px;
  margin-right: -40px;
  color: #3D405B;
}

.info {
  display: flex;
  align-items: center;
  background: #81b29a;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  padding: 100px;
  margin: 0 20px 50px 20px;
  border-radius: 20px;
}

.image3 {
  width: 450px;
}

.base2 {
  margin: 0 -20px 0 50px;
  font-size: 45px;
  line-height: 60px;
  color: #3D405B;
}

.title {
  margin-bottom: 30px;
}

.text {
  font-size: 36px;
}

.error {
  max-width: 100%;
  color: #cb0606;
  white-space: pre-wrap;
}
</style>