<template>
  <nav-bar></nav-bar>
  <div class="container">
    <div class="go-back" @click="goBack">
      <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 92 92">
        <path
            d="M84 46c0 2.2-1.8 4-4 4H21.6l18.1 18.2c1.6 1.6 1.6 4.1 0 5.7-.7.7-1.7 1.1-2.8 1.1-1 0-2.1-.4-2.8-1.2l-24.9-25c-1.6-1.6-1.6-4.1 0-5.6l24.9-25c1.6-1.6 4.1-1.6 5.7 0 1.6 1.6 1.6 4.1 0 5.7L21.6 42H80c2.2 0 4 1.8 4 4z"/>
      </svg>
      <span class="fs-5">Вернуться назад</span>
    </div>
    <!--    <button>-->
    <!--      Назад-->
    <!--    </button>-->
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
              </div>
            </div>
            <div class="card-text">
              <p class="text">Описание:
                <span v-if="!product.description" class="text-muted">Пусто</span>
                <span v-else>{{ product.description }}</span>
              </p>
            </div>
            <div class="mt-auto">
              <p class="text">Продавец: {{ product.seller }}</p>
              <p class="text">Корпус: {{ product.building }}</p>
              <p class="text">Количество: {{ product.quantity }}</p>
              <div class="d-flex align-items-center">
                <p class="fs-2 m-0">{{ product.price }}₽</p>
                <div v-if="checkProductSeller(product.seller_id)"></div>
                <green-button
                    v-else-if="checkPresenceInCart(product)"
                    @click="addToCart(product)"
                    @click.stop
                    class="ms-auto"
                ><span class="text">В корзину</span>
                </green-button>
                <button
                    v-else
                    @click="removeFromCart(product)"
                    @click.stop
                    class="green-button-outline ms-auto"
                ><span class="text">Добавлен</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <my-footer></my-footer>
</template>

<script>
import NavBar from "@/components/NavBar";
import MyFooter from '@/components/UI/MyFooter'
import axios from "axios";
import MyButton from "@/components/UI/MyButton";
import CartMethods from "@/mixins/CartMethods";
import GreenButton from "@/components/UI/GreenButton";

export default {
  name: "ProductDetail",
  components: {GreenButton, MyButton, NavBar, MyFooter},
  data() {
    return {
      product: {},
      product_slug: this.$route.params.slug,
    }
  },
  mixins: [CartMethods],
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
    beforeRouteEnter(to, from, next) {
      console.log(from);
    },
    //
    // goBack() {
    //   this.$router.push(this.$router)
    // }
  },
  watch: {
    '$route.params.slug': {
      handler(newValue) {
        this.product_slug = newValue
        this.getProduct()
      },
    }
  }
}
</script>

<style scoped>
.card {
  background-color: #f1f0e8;
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

.green-button-outline {
  display: flex;
  min-height: 39px;
  align-items: center;
  border: 2px solid #81b29a;
  border-radius: 5px;
  background-color: #bddccc;
  padding: 3px 10px;
  transition: all .3s;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}

.green-button-outline:active {
  background-color: #81b29a;
}

.go-back {

}
</style>