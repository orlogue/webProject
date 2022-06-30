<template>
  <nav-bar></nav-bar>
  <div class="container">
    <div class="row">
      <products-sidebar
          :building="this.filters.building"
          @buildingChange="this.filters.building = $event"
          :chosen-category="this.filters.chosenCategory"
          @chooseCategory="this.filters.chosenCategory = $event"
          :sort-product="this.filters.sortProduct"
          @sortProducts="this.filters.sortProduct = $event"
          @removeFilters="removeFilters"
      ></products-sidebar>
      <div class="row ms-4 row-cols-2 col-9 flex-fill">
        <div
            class="col"
            v-for="product in latestProducts"
            v-bind:key="product.id"
        >
          <div class="card mb-4"
               @click="$router.push({ name: 'ProductDetail', params: { slug: product.slug }})"
          >
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
                    </div>
                  </div>
                  <div class="card-text">
                    {{ truncate }}
                    <p class="text fs-6">{{ product.truncatedDescription }}</p>
                  </div>
                  <div class="mt-auto">
                    <p class="text">Продавец: {{ product.seller }}</p>
                    <p class="text">Корпус: {{ product.building }}</p>
                    <div class="d-flex align-items-center">
                      <p class="fs-2 m-0">{{ product.price }}₽</p>
                      <green-button
                          v-if="checkPresenceInCart(product)"
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
import GreenButton from "@/components/UI/GreenButton";
import RedButton from "@/components/UI/RedButton";
import CartMethods from "@/mixins/CartMethods";

export default {
  name: 'ProductsList',
  components: {RedButton, GreenButton, NavBar, MyFooter, SecondButton, ProductsSidebar},
  data() {
    return {
      dialogVisible: false,
      latestProducts: [],
      filters: {
        building: "",
        chosenCategory: "0",
        sortProduct: "newFirst",
      }
    }
  },
  mixins: [CartMethods],
  mounted() {
    this.getLatestProducts();
    if (localStorage.getItem('filters')) {
      this.filters = JSON.parse(localStorage.getItem('filters'))
    } else {
      localStorage.setItem('filters', JSON.stringify(this.filters))
    }
  },
  methods: {
    showDialog() {
      this.dialogVisible = true;
    },
    async getLatestProducts() {
      if (localStorage.getItem('filters'))
        this.filters = JSON.parse(localStorage.getItem('filters'))
      if (this.filters.building === "") {
        await axios
            .get('api/users/me/')
            .then(response => {
              this.filters.building = response.data['building']
            })
            .catch(error => {
              console.log(error)
            })
      }
      await axios
          .get(`/api/products/?building=${this.filters.building
          }&category=${this.filters.chosenCategory
          }&sort=${this.filters.sortProduct}`)
          .then(response => {
            this.latestProducts = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    removeFilters() {
      this.filters = {
        building: '',
        chosenCategory: '0',
        sortProduct: 'newFirst',
      }
    }
  },
  watch: {
    'filters.building'() {
      localStorage.setItem('filters', JSON.stringify(this.filters))
      this.getLatestProducts()
    },
    'filters.chosenCategory'() {
      localStorage.setItem('filters', JSON.stringify(this.filters))
      this.getLatestProducts()
    },
    'filters.sortProduct'() {
      localStorage.setItem('filters', JSON.stringify(this.filters))
      this.getLatestProducts()
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

.green-button-outline {
  display: flex;
  align-items: center;
  max-height: 33px;
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
</style>