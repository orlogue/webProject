<template>
  <div class="sidebar col-md-3 col-sm-2">
    <div>
      <second-button
          class="btn_menu1 me-2 mb-2"
          @click="$router.push({ name: 'Category' })"
      >
        Категории
      </second-button>
      <second-button
          class="btn_menu2"
          @click="$router.push({ name: 'Products'})"
      >
        Все товары
      </second-button>
    </div>
    <div class="filter mt-2">
      <div class="filter-title mb-2">
        Фильтрация
      </div>
      <div class="d-flex mb-2">
        <span class="fs-5 me-2">Корпус</span>
        <custom-select>
          <option selected>{{ this.userBuilding }}</option>
          <option v-for="building in buildings"
                  :key="building.id">
            {{ building.name }}
          </option>
          <option>Все</option>
        </custom-select>
      </div>
      <div class="d-flex">
        <span class="fs-5 me-2">Категория</span>
        <custom-select>
          <option selected>Все</option>
          <option v-for="category in categories"
                  :key="category.id">
            {{ category.name }}
          </option>
        </custom-select>
      </div>
    </div>

  </div>
</template>

<script>
import SecondButton from "@/components/UI/SecondButton";
import CustomSelect from "@/components/UI/CustomSelect";
import axios from "axios";

export default {
  name: "ProductsSidebar",
  data() {
    return {
      buildings: [],
      categories: [],
      userBuilding: Object,
    }
  },
  mounted() {
    this.getBuildings()
    this.getUserBuilding()
    this.getCategories()
  },
  components: {
    SecondButton, CustomSelect,
  },
  methods: {
    async getBuildings() {
      await axios
          .get('api/buildings/')
          .then(response => {
            this.buildings = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    async getUserBuilding() {
      await axios
          .get('api/users/me/')
          .then(response => {
            this.userBuilding = response.data['building']
          })
          .catch(error => {
            console.log(error)
          })
    },
    async getCategories() {
      await axios
          .get('/api/category/')
          .then(response => {
            this.categories = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
  }
}

</script>

<style scoped>
.btn_menu1 {
  margin: 0;
  font-size: 20px;
  background-color: #f4f1de;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 5px;
}

.btn_menu2 {
  font-size: 20px;
  background-color: #f4f1de;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 5px;
}

.filter {
  max-width: 243px;
}

.filter-title {
  display: inline-block;
  margin: 0;
  border-radius: 5px;
  width: 100%;
  background-color: #E07A5F;
  padding: 10px;
}

.sidebar {
  display: flex;
  flex-direction: column;
}
</style>