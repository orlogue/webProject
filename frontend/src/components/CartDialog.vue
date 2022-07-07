<template>
  <div class="cart">
    <p class="fs-2 mb-4">Корзина</p>
    <div v-if="!cart.items.length">
      <p class="fs-4">Здесь пока что пусто :(</p>
    </div>
    <div v-else>
      <div class="row mb-2"
           v-for="item in cart.items"
           :key="item.product.id"
      >
        <div class="col-2">
          <img class="img-thumbnail" v-if="item.product.image" :src="item.product.image" alt="">
          <img class="img-thumbnail" v-else src="@/static/default.jpg" alt="">
        </div>
        <div class="col">
          <div class="d-flex">
            <router-link class="name fs-5 m-0"
                         :to="{ name: 'ProductDetail',
                       params: { slug: item.product.slug }}"
            >
              {{ item.product.name }}
            </router-link>
            <red-button @click="removeFromCart(item.product)"
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
              <p class="text">Цена: {{ getItemTotal(item) }}₽</p>
            </div>
            <div class="col-3">
            </div>
          </div>
        </div>
      </div>
      <div class="d-flex align-items-center mb-2">
        <div class="ms-auto fs-4">
          Итого: {{ this.getTotalSum }}₽
        </div>
        <green-button class="ms-3 fs-5"
                      @click="submitOrder"
        >
          Оформить заказ
        </green-button>
      </div>
    </div>
  </div>
</template>

<script>
import RedButton from "@/components/UI/RedButton";
import GreenButton from "@/components/UI/GreenButton";
import CartMethods from "@/mixins/CartMethods";
import axios from "axios";

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
  mixins: [CartMethods],
  computed: {
    getTotalSum() {
      let sum = 0
      this.cart.items.forEach(item => sum += this.getItemTotal(item))
      return sum
    }
  },
  mounted() {
    this.cart = this.$store.state.cart;
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
    async submitOrder() {
      let formData = new FormData()
      formData.append('buyer', this.$root.profile.id)

      await axios
          .post('api/order/', formData)
          .then(response => {
            if (response.status === 201) {
              this.cart.items.forEach(item => {
                formData = new FormData()
                formData.append('product', item.product.id)
                formData.append('quantity', item.quantity)
                formData.append('order', response.data.id)
                axios
                    .post('api/order/item/', formData)
                    .catch(error => {
                      console.log(error)
                    })
              })
              this.$store.commit('clearCart')
              this.cart = this.$store.state.cart
            }
          })
          .catch(error => {
            console.log(error)
          })
    }
  },
}
</script>

<style scoped>
.name {
  text-underline-offset: 2px;
  color: black;
}

.cart {
  width: 600px;
  padding: 0 10px;
}

.text {
  font-size: 16px;
}
</style>