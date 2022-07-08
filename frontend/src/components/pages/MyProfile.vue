<template>
  <nav-bar>
  </nav-bar>
  <div class="container">
    <div class="row mt-2">
      <div class="col cols-4 d-flex flex-column">
        <div class="card mb-4">
          <div class="card-header ps-3 py-2 d-flex">
            <h3 style="margin-bottom: 0;">
              Информация
            </h3>
            <my-button class="edit ms-auto align-self-center"
                       @click="changeProfileData"
                       v-if="!editing"
            >Редактировать
            </my-button>
            <div v-else
                 class="d-flex flex-fill justify-content-end"
            >
              <red-button
                  class="align-self-center"
                  @click="editing = false"
              >Отменить
              </red-button>
              <green-button
                  class="ms-2 align-self-center"
                  @click="submitChanges"
              >Принять
              </green-button>
            </div>
          </div>
          <div class="card-body">
            <div class="row mb-2">
              <span class="col-5 fs-5">Имя: </span>
              <span v-if="!editing" class="col-7 fs-5">{{ profile.name }}</span>
              <input v-else type="text" class="col-7 fs-5" v-model="newProfile.name">
            </div>
            <div class="row mb-2">
              <span class="col-5 fs-5">Номер: </span>
              <span class="col-7 fs-5">{{ profile.phone_number }}</span>
            </div>
            <div class="row mb-2">
              <span class="col-5 fs-5">Корпус: </span>
              <span v-if="!editing" class="col-7 fs-5">{{ profile.building }}</span>
              <select v-else class="col-7 fs-5" @change="setBuilding($event)">
                <option selected disabled>Выберите корпус</option>
                <option v-for="building in buildings"
                        :key="building.id"
                        :value="building.name"
                        :selected="building.name === newProfile.building"
                >{{ building.name }}
                </option>
              </select>
            </div>
            <div class="row">
              <div class="col-5 fs-5">Комната:</div>
              <span v-if="!editing" class="col-7 fs-5">{{ profile.room }}</span>
              <input v-else type="text" class="col-7 fs-5" v-model="newProfile.room">
            </div>
          </div>
        </div>
      </div>
      <div class="col col-lg-8 d-flex flex-column">
        <div class="card fs-5 mb-4">
          <div class="card-header ps-3 py-2">
            <h3 style="margin-bottom: 0;">
              Мои товары
            </h3>
          </div>
          <div class="card-body scrollable-list">
            <div v-for="product in products"
                 :key="product.id"
                 class="card card-item col-7 me-3"
            >
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
                  <div class="card-body card-body-item d-flex flex-column">
                    <div class="card-title m-0 fs-4">
                      <!--                         @click="$router.push({ name: 'ProductDetail', params: { slug: product.slug }})"-->
                      <div class="d-flex justify-content-between align-items-center">
                        <a class="clickable name"
                           @click="$router.push({ name: 'ProductDetail',
                              params: { slug: product.slug }})"
                        >{{ product.name }}</a>
                        <div class="dropdown">
                          <button class="dropdown-icon" type="button" id="dropdownMenuButton1"
                                  data-bs-toggle="dropdown" aria-expanded="false">
                            <ThreeDots></ThreeDots>
                          </button>
                          <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
                            <li>
                              <button class="dropdown-item"
                                      @click="editProduct(product)"
                              >Изменить
                              </button>
                            </li>
                            <li>
                              <button class="dropdown-item"
                                      @click="deleteProduct(product.slug)"
                              >Удалить
                              </button>
                            </li>
                          </ul>
                        </div>
                      </div>

                    </div>
                    <p class="fs-6 m-0">Категория: {{ product.category_name }}</p>
                    <div class="card-text">
                      {{ truncate }}
                      <span class="fs-6 m-0">Описание: </span>
                      <span class="fs-6">{{ product.truncatedDescription }}</span>
                    </div>
                    <div class="mt-auto">
                      <p class="fs-5 m-0">Количество: {{ product.quantity }} шт. </p>
                      <p class="fs-5 m-0">Цена: {{ product.price }}₽ </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="card fs-5 mb-4">
          <div class="card-header ps-3 py-2 d-flex align-items-center">
            <h3 style="margin-bottom: 0;">
              История заказов
            </h3>
            <nav v-if="products.length"
                 class="ms-auto">
              <ul class="pagination mb-0">
                <li class="page-item">
                  <button class="page-link"
                          @click="page--"
                          :class="page === 1 ? 'disabled': ''"
                  >
                    <span aria-hidden="true">Назад</span>
                  </button>
                </li>
                <li class="page-item">
                  <button class="page-link"
                          @click="page++"
                          :class="showNextButton ? '' : 'disabled'"
                  >
                    <span aria-hidden="true">Вперёд</span>
                  </button>
                </li>
              </ul>
            </nav>
          </div>
          <div class="card-body orders pt-3 px-4">
            <div class="row mb-3"
                 v-for="order in orders"
                 :key="order.id"
            >
              <div class="card order">
                <div class="card-title my-2">Заказ: {{ order.id }}</div>
                <div class="row mb-2"
                     v-for="item in order.items"
                     :key="item.id">
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
                    </div>
                    <div class="row align-items-center">
                      <div class="col-5">
                        <p class="text">Продавец: {{ item.product.seller }}</p>
                        <p class="text">Корпус: {{ item.product.building }}</p>
                      </div>
                      <div class="col-4">
                        <div class="d-flex align-items-center">
                          <span class="text me-2">Количество: {{ item.quantity }}</span>
                        </div>
                        <p class="text">Цена: {{ item.product.price * item.quantity }}₽</p>
                      </div>
                      <div class="col-3">
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <my-footer></my-footer>

  <edit-product-dialog :product="product"
                       :visible="editDialog"
                       @updateVisible="closeDialog"
  >
  </edit-product-dialog>
</template>

<script>

import NavBar from "@/components/NavBar";
import MyFooter from "@/components/UI/MyFooter";
import API from "@/mixins/API";
import axios from "axios";
import MyButton from "@/components/UI/MyButton";
import RedButton from "@/components/UI/RedButton";
import GreenButton from "@/components/UI/GreenButton";
import EditProductDialog from "@/components/editProductDialog";
import PopupDialog from "@/components/UI/PopupDialog";
import ThreeDots from "@/components/UI/ThreeDots";

export default {
  components: {
    ThreeDots,
    PopupDialog,
    GreenButton,
    RedButton,
    MyButton,
    NavBar,
    MyFooter,
    EditProductDialog
  },
  mixins: [API],
  data() {
    return {
      profile: {},
      newProfile: {},
      editing: false,
      buildings: [],
      products: [],
      product: {},
      editDialog: false,
      orders: [],
      page: 1,
      showNextButton: false,
    }
  },
  mounted() {
    this.getProfile()
    this.getBuildings()
    this.getMyProducts()
    this.getOrders()
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
  },
  methods: {
    setBuilding(e) {
      this.newProfile.building = e.target.value
    },
    changeProfileData() {
      this.newProfile = this.profile
      this.editing = true
    },
    editProduct(product) {
      this.product = Object.assign({}, product)
      this.editDialog = true
    },
    closeDialog() {
      this.editDialog = false
      this.getMyProducts()
    },
    async deleteProduct(slug) {
      await axios
          .delete(`api/products/${slug}`)
          .then(() => {
            this.getMyProducts()
          })
          .catch(error => {
            console.log(error)
          })
    },
    async submitChanges() {
      this.editing = false
      await axios
          .put('api/users/me/', this.newProfile)
          .catch(error => {
            console.log(error)
          })
    },
    async getMyProducts() {
      await axios
          .get('api/products/mine/')
          .then(response => {
            this.products = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    async getOrders() {
      await axios
          .get(`api/order/mine/?page=${this.page}`)
          .then(response => {
            response.data.next ? this.showNextButton = true : this.showNextButton = false;
            this.orders = response.data.results
          })
          .catch(error => {
            console.log(error)
          })
    }
  },
  watch: {
    page() {
      this.getOrders()
    }
  }
}
</script>

<style scoped>
.card {
  background-color: #f1f0e8;;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 8px;
}

.orders {
  margin-right: 0 !important;
}

.card-body {
  padding: 10px;
  margin-right: 12px;
}

.card-body > .row {
  align-items: center;
}

.scrollable-list {
  display: flex;
  margin-right: 0;
  padding: 16px;
  overflow: auto;
}

.card-item:last-child {
  margin-right: 0 !important;
}

.edit {
  border-radius: 8px;
  border-style: none;
  background-color: #f5f4f1;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  padding: 3px 10px;
}

.edit:active {
  background-color: #dadad5;
}

input {
  height: 100%;
}

select {
  max-height: 30.5px;
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

.card {
  background-color: #f1f0e8;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
  transition: all .3s;
}

.card-item {
  max-height: 220px;
}

.card-item:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.card-body-item {
  min-height: 220px;
}


.dropdown-icon {
  border-style: none;
}

#dropdownMenuButton1 {
  background-color: transparent;
}

.text {
  font-size: 18px;
}

.name {
  text-underline-offset: 2px;
  color: black;
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