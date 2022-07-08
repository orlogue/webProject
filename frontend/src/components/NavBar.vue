<template>
  <div class="navbar py-3 px-4">
    <div @click="isAuthenticated
    ? this.$router.push({ name: 'Products'})
    : this.$router.push({ name: 'Home' })" class="logo me-4"
    >
      <strong>FEFU market</strong>
    </div>
    <my-button
        @click="productCreateDialog"
        class="nav-button me-auto align-self-center"
    >
      Разместить товар
    </my-button>
    <div class="align-items-center">
      <my-button
          @click="cartDialog"
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
  <popup-dialog :show="cartVisible"
                @updateShow="closeDialog"
  >
    <cart-dialog></cart-dialog>
  </popup-dialog>
  <popup-dialog :show="productCreateVisible"
                @updateShow="closeDialog"
  >
    <new-product-dialog></new-product-dialog>
  </popup-dialog>
</template>

<script>
import PopupDialog from "@/components/UI/PopupDialog";
import MyButton from "@/components/UI/MyButton";
import SecondButton from "@/components/UI/SecondButton";
import CartDialog from "@/components/CartDialog";
import axios from "axios";
import NewProductDialog from "@/components/NewProductDialog";

export default {
  components: {NewProductDialog, MyButton, PopupDialog, SecondButton, CartDialog},
  data() {
    return {
      cartVisible: false,
      productCreateVisible: false,
      isAuthenticated: this.$store.state.isAuthenticated,
    }
  },
  methods: {
    cartDialog() {
      this.cartVisible = true;
      document.querySelector('body').style.overflow = 'hidden';
    },
    productCreateDialog() {
      this.productCreateVisible = true;
      document.querySelector('body').style.overflow = 'hidden';
    },
    closeDialog() {
      this.cartVisible = false;
      this.productCreateVisible = false
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
}
</style>