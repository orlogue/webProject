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
              <!--              <input v-else type="text" class="col-7 fs-5" v-model="newProfile.phone_number">-->
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
                        {{ product.name }}
                        <div class="dropdown">
                          <button class="dropdown-icon" type="button" id="dropdownMenuButton1"
                                  data-bs-toggle="dropdown" aria-expanded="false">
                            ...
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
        <div class="card fs-5">
          <div class="card-header ps-3 py-2">
            <h3 style="margin-bottom: 0;">
              История заказов
            </h3>
          </div>
          <div class="row px-3">
            <div class="col col-lg-2 col-sm-3 p-0 flex-fill">
              <span class="list-group-item">Заказы</span>
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

export default {
  components: {PopupDialog, GreenButton, RedButton, MyButton, NavBar, MyFooter, EditProductDialog},
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
    }
  },
  mounted() {
    this.getProfile()
    this.getBuildings()
    this.getMyProducts()
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
          .get('api/products/mine')
          .then(response => {
            this.products = response.data
          })
          .catch(error => {
            console.log(error)
          })
    }
  }
}
</script>

<style scoped>
.card {
  /*max-width: 243px;*/
  background-color: #f1f0e8;;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 5px;
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
  /*max-height: 330px;*/
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
  /*background-color: ;*/
  /*align-self: center;*/
  /*display: inline-block;*/
  /*text-align: center;*/
  /*line-height: 1px;*/
  /*margin: auto;*/
  /*padding: 0;*/
}
</style>