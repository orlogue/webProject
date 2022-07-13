<template>
  <router-view></router-view>
</template>

<script>
import axios from 'axios'
import API from "@/mixins/API";

export default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      },
      isAuthenticated: false,
      profile: {}
    }
  },
  mixins: [API],
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
      axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
    if (this.$store.state.isAuthenticated) {
      this.getProfile()
      this.isAuthenticated = this.$store.state.isAuthenticated
    }
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.length
    }
  },
  watch: {
    '$store.state.isAuthenticated'(to, from) {
      if (to === false) {
        this.isAuthenticated = false
        this.profile = {}
      } else {
        this.getProfile()
        this.isAuthenticated = this.$store.state.isAuthenticated
      }
    },
    '$store.state.cart.items'() {
      this.cart = this.$store.state.cart
    }
  }
}
</script>

<style>

@import url('https://fonts.googleapis.com/css2?family=Ruda&display=swap');

body {
  background-image: url('@/static/2.jpg');
  background-repeat: no-repeat;
  background-color: #F4F1E0 !important;
  margin: 0;
  padding: 0;
  font-family: 'Ruda', Arial, Helvetica, sans-serif !important;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}

#app {
  /*background-color: #F4F1E0;*/
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.container, .container-xl {
  padding-top: 100px;
  flex-grow: 1;
}

input, textarea, select {
  border-radius: 8px;
  border-style: none;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  padding: 3px 10px;
  color: #212529;
}

a, button {
  color: #212529;
}

input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type=number] {
  -moz-appearance: textfield;
}

.nav-button {
  font-size: 25px;
  color: #3D405B;
}

.clickable {
  cursor: pointer;
}

.logo {
  font-size: 38px;
  color: #3D405B;
  margin-left: 10px;
}

nav, ul.pagination, ul.pagination > li.page-item {
  background-color: transparent !important;
  border-radius: 15px !important;
}

ul.pagination > li.page-item {
  background-color: #f5f4f1 !important;
}

nav > ul.pagination {
  display: inline-flex;
  width: auto;
}

nav > .pagination {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.page-link {
  color: black;
  background-color: #f5f4f1;
}

.page-link:hover {
  background-color: inherit;
  text-decoration: none;
  color: black !important;
}

.disabled {
  background-color: #f5f4f1 !important;
}

.page-link:focus, .page-link:active {
  outline: none !important;
  box-shadow: none;
}

.page-link:active {
  background-color: #dadad5;
  color: black !important;
}
</style>