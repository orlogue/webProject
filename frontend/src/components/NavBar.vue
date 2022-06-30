<template>
  <div class="navbar py-3 px-4">
    <div @click="isAuthenticated
    ? this.$router.push({ name: 'Products'})
    : this.$router.push({ name: 'Home' })" class="logo"
    >
      <strong>FEFU market</strong>
    </div>
    <div class="">
      <my-button
          @click="showDialog"
          class="entrance1"
      ><img class="image4" src="@/static/4.png" alt="">
        {{ $root.cartTotalLength }}
      </my-button>
      <my-button
          @click="$router.push('/profile')"
          class="entrance"
      >Мой профиль
      </my-button>
      <my-button
          @click="logOut"
          class="entrance"
      >Выйти
      </my-button>
    </div>
  </div>
  <my-window :show="dialogVisible"
             @updateShow="closeDialog($event)"
  >
    <cart-dialog></cart-dialog>
  </my-window>
</template>

<script>
import MyWindow from "@/components/UI/MyWindow";
import MyButton from "@/components/UI/MyButton";
import SecondButton from "@/components/UI/SecondButton";
import CartDialog from "@/components/CartDialog";
import axios from "axios";

export default {
  components: {MyButton, MyWindow, SecondButton, CartDialog},
  data() {
    return {
      dialogVisible: false,
      isAuthenticated: this.$store.state.isAuthenticated
    }
  },
  methods: {
    showDialog() {
      this.dialogVisible = true;
      document.querySelector('body').style.overflow = 'hidden';
    },
    closeDialog(bool) {
      this.dialogVisible = bool;
      document.querySelector('body').removeAttribute('style')
    },
    async logOut() {
      await axios
          .post('/auth/token/logout/', localStorage.getItem('token'))
          .then(() => {
            this.$store.commit('removeToken')
            localStorage.removeItem('token')
            this.$router.push('/')
          })
          .catch(error => {
            console.log(JSON.stringify(error))
          })
    },
  },
}
</script>

<style scoped>
.logo {
  text-decoration: none;
  cursor: pointer;
}

.logo:active, :hover {
  color: #0b182c;
}

.image4 {
  width: 30px;
}

.navbar {
  display: flex;
  flex-direction: row;
}
</style>