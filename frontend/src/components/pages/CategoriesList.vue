<template>
  <nav-bar></nav-bar>
  <div class="container">
    <div class="row">
      <products-sidebar></products-sidebar>
      <div class="category ms-4 col-8">
        <div class="square1"
             v-for="category in categories"
             v-bind:key="category.id"
             @click="getSubcategories(category)"
        >
          {{ category.name }}
          <!--          require(`@/static/${category.slug}.png`) || -->
          <img class="ic1"
               :src="require('@/static/default.jpg')" :alt="category.slug"
          >
          <router-link :to="{ name: 'Category', params: { slug: category.slug }}"
          ></router-link>
        </div>
      </div>
    </div>
  </div>
  <my-footer></my-footer>
</template>

<script>
import MyFooter from "@/components/UI/MyFooter";
import NavBar from "@/components/NavBar";
import SecondButton from "@/components/UI/SecondButton";
import ProductsSidebar from "@/components/UI/ProductsSidebar";
import axios from 'axios'

export default {
  components: {NavBar, MyFooter, SecondButton, ProductsSidebar},
  data() {
    return {
      categories: [],
      currentCategory: Object,
    }
  },
  mounted() {
    this.getCategories()
  },
  methods: {
    getCategories() {
      axios
          .get('/api/category/')
          .then(response => {
            this.categories = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    getSubcategories(category) {
      this.currentCategory = category
      console.log(this.currentCategory)
      const path = this.$route.path
      this.$router.push(`${path}/${category.slug}`)
      axios
          .get(`/api/category/${category.id}/subcategory`)
          .then(response => {
            this.categories = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
  },
  watch: {
    $route(to, from) {
      if (to.path === '/category') {
        this.getCategories();
      }
    }
  }
}

</script>

<style scoped>
.square1 {
  background-color: #f4f1de;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 10px;
  font-size: 20px;
  width: 190px;
  height: 190px;
  padding: 20px;
  margin-right: 70px;
  margin-bottom: 70px;
  transition: all .6s;
  text-align: center;
  cursor: pointer;
}

.square1:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
}

.category {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
}

.item.new-string {
  width: 100%;
}

.ic1 {
  height: 75%;
}
</style>