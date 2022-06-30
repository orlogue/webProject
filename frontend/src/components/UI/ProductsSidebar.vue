<template>
  <div class="sidebar col-md-3 col-sm-2">
    <div class="d-flex">
      <second-button
          class="btn_menu1 mb-2"
          @click="$router.push({ name: 'Category' })"
      >
        Категории
      </second-button>
      <second-button
          class="btn_menu2 ms-auto mb-2"
          @click="goToProducts"
      >
        Все товары
      </second-button>
    </div>
    <div class="filter mt-2">
      <div class="filter-title">
        Фильтрация
      </div>
      <div class="filter-body">
        <div class="filter-item">
          <span class="me-2">Корпус</span>
          <custom-select @change="changeBuilding"
          >
            <option
                v-for="building in buildings"
                :key="building.id"
                :value="building.name"
                :selected="building.name === translate()"
            >
              {{ building.name }}
            </option>
            <option value="all">Все</option>
          </custom-select>
        </div>
        <div class="filter-item">
          <span class="me-2">Категория</span>
          <custom-select @change="chooseCategory">
            <option value="0" :selected="chosenCategory === '0'">Все</option>
            <option v-for="category in categories"
                    :key="category.id"
                    :value="category.id"
                    :selected="category.id === +chosenCategory"
            >
              {{ category.name }}
            </option>
          </custom-select>
        </div>
        <div class="filter-item">
          <span class="me-2">Cначала</span>
          <custom-select @change="sort">
            <option value="newFirst" :selected="sortProduct === 'newFirst'">Новые</option>
            <option value="oldFirst" :selected="sortProduct === 'oldFirst'">Старые</option>
            <option value="cheapFirst" :selected="sortProduct === 'cheapFirst'">Дешёвые</option>
            <option value="expensiveFirst" :selected="sortProduct === 'expensiveFirst'">Дорогие</option>
          </custom-select>
        </div>
      </div>
    </div>
    <button
        class="discard-filters btn_menu1 mt-3"
        @click="removeFilters"
    >
      Сбросить фильтры
    </button>
  </div>
</template>

<script>
import SecondButton from "@/components/UI/SecondButton";
import CustomSelect from "@/components/UI/CustomSelect";
import axios from "axios";
import MyButton from "@/components/UI/MyButton";

export default {
  name: "ProductsSidebar",
  data() {
    return {
      buildings: [],
      categories: [],
    }
  },
  mounted() {
    this.getBuildings()
    this.getCategories()
  },
  components: {
    MyButton,
    SecondButton, CustomSelect,
  },
  props: ['building', 'chosenCategory', 'sortProduct'],
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
    async getCategories() {
      await axios
          .get('/api/category/subcategory/')
          .then(response => {
            this.categories = response.data
          })
          .catch(error => {
            console.log(error)
          })
    },
    changeBuilding(e) {
      this.$emit('buildingChange', e.target.value)
    },
    chooseCategory(e) {
      this.$emit('chooseCategory', e.target.value)
    },
    sort(e) {
      this.$emit('sortProducts', e.target.value)
    },
    translate() {
      if (this.building === 'all')
        return 'Всe'
      else
        return this.building
    },
    goToProducts() {
      this.$router.push({name: 'Products'})
    },
    removeFilters() {
      this.$emit('removeFilters')
      // if (localStorage.getItem('filters')) {
      //   localStorage.removeItem('filters')
      // }
    }
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
  /*max-width: 243px;*/
  background-color: #f4f1de;;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 5px;
}

.filter-title {
  margin: 0;
  width: 100%;
  font-size: 20px;
  padding: 5px 10px;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  background-color: #ea866b;
}

.filter-body {
  padding: 15px 10px;
}

.filter-item {
  display: flex;
  font-size: 18px;
  margin-bottom: 1em;
}

.filter-item:last-child {
  margin-bottom: 0;
}

.sidebar {
  display: flex;
  flex-direction: column;
  max-width: 275px;
}

.discard-filters {
}
</style>