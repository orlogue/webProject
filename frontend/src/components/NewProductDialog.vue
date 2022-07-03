<template>
  <div class="product-create-dialog">
    <p class="fs-2 mb-4">Размещение товара</p>
    <form class="row" @submit.prevent="submitForm" enctype="multipart/form-data">
      <div class="col-3">
        <img class="img-fluid" src="@/static/default.jpg" alt="">
        <input class="mt-3" type="file" accept="image/*" @change="onSelectedFile($event)">
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
        <div class="row">
          <green-button class="submit-button mt-2">
            <span class="fs-4">Разместить</span>
          </green-button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import API from "@/mixins/API";
import GreenButton from "@/components/UI/GreenButton";
import axios from "axios";

export default {
  name: "NewProductDialog",
  components: {GreenButton},
  mixins: [API],
  data() {
    return {
      categories: [],
      product: {
        name: '',
        description: '',
        category: 1,
        seller: this.$root.profile.id,
        quantity: 1,
        price: '',
        image: null,
      }
    }
  },
  mounted() {
    this.categories = this.getCategories();
  },
  methods: {
    setCategory(e) {
      this.product.category = +e.target.value
    },
    onSelectedFile(e) {
      this.product.image = e.target.files[0]
      console.log(this.product.image)
    },
    async submitForm() {
      const formData = new FormData()
      formData.append('name', this.product.name)
      formData.append('description', this.product.description)
      formData.append('category', this.product.category)
      formData.append('seller', this.product.seller)
      formData.append('quantity', this.product.quantity)
      formData.append('price', this.product.price)
      formData.append('image', this.product.image)

      await axios
          .post('api/products/create', formData)
          .then(response => {
            this.$router.push({ name: 'ProductDetail', params: { slug: response.data.slug }})
          })
          .catch(error => {
            console.log(error)
          })
    }
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
.submit-button {
  width: auto;
  margin-left: auto;
}
</style>