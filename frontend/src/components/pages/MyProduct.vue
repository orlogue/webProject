<template>
  <nav-bar></nav-bar>
  <div class="container">
    <div class="row">
      <products-sidebar></products-sidebar>
      <div class="row row-cols-2 col-9 flex-fill">
        <div
            class="col"
            v-for="product in latestProducts"
            v-bind:key="product.id"
        >
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
                      <span class="fs-4 m-0">{{ product.name }}</span>
                      <!--                      <span class="fs-4 m-0">ВРЕМЯ</span>-->
                    </div>
                  </div>
                  <div class="card-text">
                    {{ truncate }}
                    <p class="text fs-6">{{ product.truncatedDescription }}</p>
                  </div>
                  <div class="mt-auto">
                    <p class="text">Продавец: {{ product.seller }}</p>
                    <p class="text">Количество: {{ product.quantity }}</p>
                    <p class="fs-3 m-0">{{ product.price }}₽</p>
                  </div>

                </div>
              </div>
            </div>
          </div>
          <!--          <router-link v-bind:to="product.get_absolute_url" class="button is-light mt-4">Подробнее</router-link>-->
        </div>
        <div v-if="!latestProducts.length" class="fs-4">
          Пока что здесь пусто :( <br>
          Подождите или попробуйте поискать в других корпусах.
        </div>
      </div>
    </div>
  </div>
  <my-footer></my-footer>
</template>

<script>
import SecondButton from "@/components/UI/SecondButton";
import MyFooter from "@/components/UI/MyFooter";
import NavBar from "@/components/NavBar";
import ProductsSidebar from "@/components/UI/ProductsSidebar";
import axios from "axios";

export default {
  components: {NavBar, MyFooter, SecondButton, ProductsSidebar},
  data() {
    return {
      dialogVisible: false,
      latestProducts: [],
    }
  },
  mounted() {
    this.getLatestProducts()
  },
  methods: {
    showDialog() {
      this.dialogVisible = true;
    },
    async getLatestProducts() {
      await axios
          .get('/api/products/')
          .then(response => {
            this.latestProducts = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
  },
  computed: {
    truncate() {
      return this.latestProducts.forEach(item => {
        if (item.description.length > 50) {
          item['truncatedDescription'] = item.description.substring(0, 50) + '...';
        } else {
          item['truncatedDescription'] = item.description
        }
      })
    }
  }
}
</script>

<style>
.card {
  background-color: #f4f1de !important;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
  min-height: 220px;
  max-height: 220px;
  transition: all .3s;
}

.card:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.card-body {
  min-height: 220px;
}

.card-text {
  flex: 100% 1 0;
  display: flex;
  flex-direction: column;
}

.img-parent {
  max-height: 220px;
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
  font-size: 18px;
  margin: 0;
}
</style>