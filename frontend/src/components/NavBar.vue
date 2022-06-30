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
          class="nav-button"
      ><img class="image4" src="@/static/4.png" alt="">
        {{ $root.cartTotalLength }}
      </my-button>
      <my-button
          @click="$router.push('/profile')"
          class="nav-button"
      >Мой профиль
      </my-button>
      <my-button
          @click="logOut"
          class="nav-button"
      >Выйти
      </my-button>
    </div>
  </div>
  <my-window :show="dialogVisible"
             @updateShow="closeDialog"
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
    closeDialog() {
      this.dialogVisible = false;
      document.querySelector('body').removeAttribute('style')
    },
    async logOut() {
      await axios
          .post('/auth/token/logout/', localStorage.getItem('token'))
          .then(() => {
            this.$store.commit('removeToken')
            this.$store.commit('clearCart')
            localStorage.removeItem('token')
            localStorage.removeItem('filters')
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