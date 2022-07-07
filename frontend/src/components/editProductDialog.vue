<template>
  <div class="dialog" v-if="visible" @click="closeDialog">
    <div @click.stop class="dialog__content d-flex flex-column">
      <button
          class="btn_close"
          @click="closeDialog"
      >
        <img class="close" src="@/static/close.png" alt="">
      </button>
      <div class="product-create-dialog">
        <p class="fs-2 mb-4">Изменение информации о товаре</p>
        <!--    <form class="row" @submit.prevent="submitForm" enctype="multipart/form-data">-->
        <div class="row">
          <div class="col-3">
            <img v-if="product.image && imageUrl === null"
                 class="img-fluid"
                 :src="product.image"
                 alt="">
            <img v-else-if="imageUrl !== null" class="img-fluid" :src="imageUrl" alt="">
            <img v-else class="img-fluid" src="@/static/default.jpg" alt="">
            <input class="mt-3 image-selector"
                   type="file"
                   accept="image/*"
                   @change="onSelectedFile($event)">
          </div>
          <div class="col">
            <div class="row mb-4">
              <span class="col-sm-4 fs-4">Название: </span>
              <input type="text" class="col-sm-8 fs-5" v-model="product.name">
            </div>
            <div class="row mb-4">
              <span class="col-sm-4 fs-4">Описание: </span>
              <textarea type="text"
                        cols="30"
                        rows="4"
                        class="col-sm-8 fs-5"
                        v-model="product.description"
              ></textarea>
            </div>
            <div class="row mb-4">
              <span class="col-sm-4 fs-4">Категория: </span>
              <!--            <input type="number" min="1" class="form-input" v-model="quantity">-->
              <select class="col-sm-8 fs-5" @change="setCategory($event)">
                <option v-for="category in categories"
                        :key="category.id"
                        :value="category.id"
                        :selected="category.id === product.category"
                >
                  {{ category.name }}
                </option>
              </select>
            </div>
            <div class="row mb-4">
              <div class="col-sm-4 fs-4">Количество:</div>
              <div class="input-group col p-0">
                <input type="number" min="0" class="col-sm-2 fs-5" v-model="product.quantity">
                <div class="input-group-text fs-6 px-2 py-1">шт.</div>
              </div>
            </div>
            <div class="row mb-4">
              <div class="col-sm-4 fs-4">Цена:</div>
              <div class="input-group col p-0">
                <input type="number" min="0" class="col-sm-3 fs-5" v-model="product.price">
                <div class="input-group-text fs-5 px-2 py-1">₽</div>
              </div>
            </div>
            <div class="row justify-content-end">
              <red-button class="button"
                          @click="closeDialog"
              >
                <span class="fs-4">Отменить</span>
              </red-button>
              <green-button class="button ms-3"
                            @click="submitForm"
              >
                <span class="fs-4">Применить</span>
              </green-button>
            </div>
          </div>
        </div>
        <!--    </form>-->
      </div>
    </div>
  </div>
</template>

<script>
import API from "@/mixins/API";
import GreenButton from "@/components/UI/GreenButton";
import RedButton from "@/components/UI/RedButton";
import axios from "axios";

export default {
  name: "EditProductDialog",
  components: {GreenButton, RedButton},
  mixins: [API],
  data() {
    return {
      categories: [],
      // updatedProduct: {},
      image: null,
      imageUrl: null,
    }
  },
  props: ['product', 'visible'],
  mounted() {
    this.categories = this.getCategories();
  },
  methods: {
    closeDialog() {
      this.$emit('updateVisible')
    },
    setCategory(e) {
      this.product.category = +e.target.value
    },
    onSelectedFile(e) {
      this.image = e.target.files[0]
      this.imageUrl = URL.createObjectURL(this.image)
    },
    async submitForm() {
      const formData = new FormData()
      // if (this.updatedProduct.name !== this.product.name)
      formData.append('name', this.product.name)
      // if (this.updatedProduct.description !== this.product.description)
      formData.append('description', this.product.description)
      // if (this.updatedProduct.category !== this.product.category)
      formData.append('category', this.product.category)
      // if (this.updatedProduct.quantity !== this.product.quantity)
      formData.append('quantity', this.product.quantity)
      // if (this.updatedProduct.price !== this.product.price)
      formData.append('price', this.product.price)
      if (this.image !== null)
        formData.append('image', this.image)

      await axios
          .patch(`api/products/${this.product.slug}/update/`, formData)
          .then(() => {
            this.closeDialog()
          })
          .catch(error => {
            console.log(error)
          })
    },
    // watch: {
    //   'product.name'(newValue) {
    //     this.updatedProduct.name = newValue
    //   }
    // }
  }
}
</script>

<style scoped>
.product-create-dialog {
  max-width: 800px;
  padding: 10px;
}

.input-group-text {
  background-color: white;
  border-style: none;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}

.col {
  margin-right: 12px;
}

.image-selector {
  max-width: 100%;
  background-color: #FFFFFF;
}

.image-selector::-webkit-file-upload-button {
  visibility: hidden;
}

.image-selector::before {
  content: 'Выберите фото';
  display: inline-block;
  white-space: nowrap;
  -webkit-user-select: none;
  cursor: pointer;
  font-size: 16px;
}


.image-selector:active {
  background-color: #dadad5;
  transition: all .3s;
}

.button {
  width: auto;
  /*line-height: 24px;*/
  /*margin-left: auto;*/
}

.dialog {
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: rgba(0, 0, 0, 0.5);
  position: fixed;
  display: flex;
}

.dialog__content {
  overflow: auto;
  margin: 30px auto auto auto;
  max-height: 90vh;
  background: #f1f0e8;
  border-radius: 12px;
  min-height: 50px;
  min-width: 300px;
  padding: 10px;
}

.close {
  width: 25px;
  border-style: none;
}

.btn_close {
  align-self: end;
  border-style: none;
  transition: all .6s;
}

.btn_close:hover {
  opacity: 0.7;
}
</style>