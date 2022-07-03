<template>
  <div class="sidebar col-lg-3 mb-5">
    <div class="d-flex">
      <second-button
          class="btn_menu mb-2 flex-fill me-2"
          @click="$router.push({ name: 'Category' })"
      >
        Категории
      </second-button>
      <second-button
          class="btn_menu mb-2 flex-fill ms-2"
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
        class="discard-filters btn_menu mt-3"
        @click="removeFilters"
    >
      Сбросить фильтры
    </button>
  </div>
</template>

<script>
import SecondButton from "@/components/UI/SecondButton";
import CustomSelect from "@/components/UI/CustomSelect";
import MyButton from "@/components/UI/MyButton";
import API from "@/mixins/API";

export default {
  name: "ProductsSidebar",
  data() {
    return {
      buildings: [],
      categories: [],
    }
  },
  mixins: [API],
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
.btn_menu {
  font-size: 20px;
  background-color: #f1f0e8;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 5px;
}

.filter {
  /*max-width: 243px;*/
  /*background-color: #f4f1de;*/
  background-color: #f1f0e8;
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
  /*max-width: 275px;*/
}

.discard-filters {
}
</style>