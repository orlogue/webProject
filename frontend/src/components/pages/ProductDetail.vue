<template>
  <nav-bar></nav-bar>
  <div class="container">
    <div class="col">
      <div class="card mb-4">
        <div class="row g-0">
          <div class="col-5 img-parent">
            <img class="img" v-if="product.image" :src="product.image" alt="">
            <img class="img" v-else src="@/static/default.jpg" alt="">
          </div>
          <div class="col-7 p-0">
            <div class="card-body d-flex flex-column">
              <div class="card-title m-0">
                <div>
                  <span class="fs-1 m-0">{{ product.name }}</span>
                  <!--                      <span class="fs-4 m-0">ВРЕМЯ</span>-->
                </div>
              </div>
              <div class="card-text">
                <p class="text">Описание:
                  <span v-if="!product.description" class="text-muted">Пусто</span>
                  <!--                  {{ product.description }}-->
                </p>
              </div>
              <div class="mt-auto">
                <p class="text">Продавец: {{ product.seller }}</p>
                <p class="text">Корпус: {{ product.building }}</p>
                <p class="text">Количество: {{ product.quantity }}</p>
                <div class="d-flex">
                  <p class="fs-2 m-0">{{ product.price }}₽</p>
                  <my-button class="ms-auto">В корзину</my-button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!--          <router-link v-bind:to="product.get_absolute_url" class="button is-light mt-4">Подробнее</router-link>-->
    </div>
  </div>
  <footer></footer>
</template>

<script>
import NavBar from "@/components/NavBar";
import MyFooter from '@/components/UI/MyFooter'
import axios from "axios";
import MyButton from "@/components/UI/MyButton";

export default {
  name: "ProductDetail",
  components: {MyButton, NavBar, MyFooter},
  data() {
    return {
      product: Object,
      product_slug: this.$route.params.slug,
    }
  },
  mounted() {
    this.getProduct()
  },
  methods: {
    async getProduct() {
      await axios
          .get(`api/products/${this.product_slug}`)
          .then(response => {
            this.product = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
  },
  watch: {
    '$route.params.slug': {
        handler(newValue) {
            this.product_slug = newValue
            this.getProduct()
        },
        // immediate: true,
    }
  }
}
</script>

<style scoped>
.card {
  background-color: #f4f1de !important;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
  min-height: 400px;
  max-height: 400px;
  max-width: 800px;
  margin: 0 auto;
  transition: all .3s;
}

.card-body {
  min-height: 400px;
}

.card-text {
  flex: 100% 1 0;
  display: flex;
  flex-direction: column;
}

.img-parent {
  max-height: 400px;
  padding: 16px 0 16px 16px !important;
  display: flex;
  align-items: center;
}

.img {
  border-radius: 5px;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.text {
  font-size: 22px;
  margin: 0;
}
</style>