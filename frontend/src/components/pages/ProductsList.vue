<template>
  <nav-bar></nav-bar>
  <div class="container-xl">
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
      <div class="row p-0 col-9">
        <div class="row row-cols-lg-2 row-cols-sm-1 flex-fill">
          <div
              class="col"
              v-for="product in products"
              v-bind:key="product.id"
          >
            <div class="card mb-4">
              <div class="row g-0">
                <div class="col-5 img-parent">
                  <img v-if="product.image"
                       @click="$router.push({ name: 'ProductDetail', params: { slug: product.slug }})"
                       class="img"
                       :src="product.image"
                       alt="">
                  <img v-else
                       @click="$router.push({ name: 'ProductDetail', params: { slug: product.slug }})"
                       class="img"
                       src="@/static/default.jpg"
                       alt="">
                </div>
                <div class="col-7 p-0">
                  <div class="card-body d-flex flex-column">
                    <div class="card-title m-0 fs-4"
                         @click="$router.push({ name: 'ProductDetail', params: { slug: product.slug }})"
                    >
                      {{ product.name }}
                    </div>
                    <div class="card-text">
                      {{ truncate }}
                      <p class="text fs-6">{{ product.truncatedDescription }}</p>
                    </div>
                    <div class="mt-auto">
                      <p class="text">Продавец: {{ product.seller }}</p>
                      <p class="text">Корпус: {{ product.building }}</p>
                      <div class="d-flex align-items-center">
                        <p class="fs-3 m-0">{{ product.price }}₽ </p>
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
          <div v-if="!products.length" class="fs-4">
            Пока что здесь пусто :( <br>
            Подождите или попробуйте поискать в других корпусах.
          </div>
        </div>
        <nav v-if="products.length" aria-label="Page navigation example"
             class="ps-4">
          <ul class="pagination">
            <li class="page-item">
              <button class="page-link"
                      aria-label="Previous"
                      @click="page--"
                      :class="page === 1 ? 'disabled': ''"
              >
                <span aria-hidden="true">Назад</span>
              </button>
            </li>
            <li class="page-item">
              <button class="page-link"
                      aria-label="Next"
                      @click="page++"
                      :class="showNextButton ? '' : 'disabled'"
              >
                <span aria-hidden="true">Вперёд</span>
              </button>
            </li>
          </ul>
        </nav>
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
import API from "@/mixins/API";

export default {
  name: 'ProductsList',
  components: {RedButton, GreenButton, NavBar, MyFooter, SecondButton, ProductsSidebar},
  data() {
    return {
      dialogVisible: false,
      products: [],
      filters: {
        building: "",
        chosenCategory: "0",
        sortProduct: "newFirst",
      },
      page: 1,
      showNextButton: false,
    }
  },
  mixins: [CartMethods, API],
  mounted() {
    this.getProducts();
    // this.getProfile();
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
    async getProducts() {
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
          }&sort=${this.filters.sortProduct
          }&page=${this.page}`)
          .then(response => {
            response.data.next ? this.showNextButton = true : this.showNextButton = false;
            this.products = response.data.results
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
      this.page = 1
      this.getProducts()
    },
    'filters.chosenCategory'() {
      localStorage.setItem('filters', JSON.stringify(this.filters))
      this.page = 1
      this.getProducts()
    },
    'filters.sortProduct'() {
      localStorage.setItem('filters', JSON.stringify(this.filters))
      this.page = 1
      this.getProducts()
    },
    page() {
      this.getProducts()
    }
  },
  computed: {
    truncate() {
      return this.products.forEach(item => {
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

<style scoped>
.row {
  margin: 0;
}

.card {
  background-color: #f1f0e8;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
  transition: all .3s;
}

.card:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.card-body {
  min-height: 220px;
}

.card-title {
  cursor: pointer;
}

.card-title:hover {
  cursor: pointer;
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
  cursor: pointer;
}

.text {
  font-size: 18px;
  margin: 0;
}

.green-button-outline, .edit-button {
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

.edit-button {
  background-color: #d4d7d5;
  border: 2px solid #acb0ae;
}

.edit-button:active {
  background-color: #acb0ae;
}

.green-button-outline:active {
  background-color: #81b29a;
}

.page-link {
  color: black;
}

.page-link:hover {
  background-color: #fff;
  text-decoration: none;
  color: black !important;
}

.page-link:focus, .page-link:active {
  outline: none !important;
  box-shadow: none;
  color: black !important;
  background-color: #f5f4f1;
}
</style>