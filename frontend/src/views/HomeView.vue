<template>
  <div class="home">

    <div class="row row-cols-4">
      <div
          class="col"
          v-for="product in latestProducts"
          v-bind:key="product.id"
      >

        <div class="img-thumbnail" v-if="product.get_image">
          <img v-bind:src="product.get_image">

        </div>
        <h3>{{ product.name }}</h3>
        <p class="text fs-5">Продавец: {{ product.seller }}</p>
        <p class="text fs-3">{{ product.price }}₽</p>
        <router-link v-bind:to="product.get_absolute_url" class="button is-light mt-4">Подробнее</router-link>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'

export default {
  name: 'HomeView',
  data () {
    return {
      latestProducts: []
    }
  },
  components: {
    HelloWorld
  },
  mounted() {
    this.getLatestProducts()
  },
  methods: {
    getLatestProducts() {
      axios
          .get('/api/v1/latest-products/')
          .then(response => {
            this.latestProducts = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    getProfiles() {
      axios
          .get('/api/v1/profiles/')
          .then(response => {
            this.profiles = response.data
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>
