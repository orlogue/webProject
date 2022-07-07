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
body {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}

#app {
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
</style>