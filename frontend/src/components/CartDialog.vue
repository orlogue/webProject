<template>
  <div class="cart">
    <h1 class="mb-4">Корзина</h1>
    <div class="row mb-4"
         v-for="item in cart.items"
         :key="item.product.id"
    >
      <div class="col-2">
        <img class="img-thumbnail" v-if="item.product.image" :src="item.product.image" alt="">
        <img class="img-thumbnail" v-else src="@/static/default.jpg" alt="">
      </div>
      <div class="col">
        <div class="d-flex">
          <router-link class="fs-5 m-0"
                       :to="{ name: 'ProductDetail',
                       params: { slug: item.product.slug }}"
          >
            {{ item.product.name }}
          </router-link>
          <red-button @click="addToCart(product)"
                      class="ms-auto"
          >Удалить
          </red-button>
        </div>
        <div class="row align-items-center">
          <div class="col-5">
            <p class="text">Продавец: {{ item.product.seller }}</p>
            <p class="text">Корпус: {{ item.product.building }}</p>
          </div>
          <div class="col-4">
            <div class="d-flex align-items-center">
              <span class="text me-2">Количество: </span>
              <select id="selection" class="text" @change="changeQuantity($event, item)">
                <option v-for="value in item.product.quantity"
                        :key="value"
                        :value="value"
                        :selected="value === item.quantity"
                >{{ value }}
                </option>
              </select>
            </div>
            <p class="text">Цена: {{ getItemTotal(item) }}</p>
          </div>
          <div class="col-3">
          </div>
        </div>
      </div>
    </div>
    <div class="d-flex align-items-center">
      <div class="ms-auto fs-4">
        Итого: {{ this.getTotalSum }}
      </div>
      <green-button class="ms-3 fs-5">
        Оформить заказ
      </green-button>
    </div>
  </div>
</template>

<script>
import RedButton from "@/components/UI/RedButton";
import GreenButton from "@/components/UI/GreenButton";

export default {
  name: "CartDialog",
  components: {GreenButton, RedButton},
  data() {
    return {
      cart: {
        items: []
      }
    }
  },
  computed: {
    getTotalSum() {
      let sum = 0
      this.cart.items.forEach(item => sum += this.getItemTotal(item))
      return sum
    }
  },
  mounted() {
    this.cart = this.$store.state.cart;
    document.querySelector('#cart').op
  },
  methods: {
    changeQuantity(e, item) {
      item.quantity = +e.target.value
      this.$store.commit('changeQuantity', item)
      // this.$store.state.cart.items
    },
    getItemTotal(item) {
      return item.quantity * item.product.price
    },
  }
}
</script>

<style scoped>
.cart {
  width: 600px;
  padding: 0 10px;
}

.text {
  font-size: 16px;
}
</style>