<template>
  <div class="sidebar col-lg-3 mb-5">
    <div class="filter">
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
    <my-button
        class="discard-filters btn_menu mt-3"
        @click="removeFilters"
    >
      Сбросить фильтры
    </my-button>
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
    }
  }
}

</script>

<style scoped>
.btn_menu {
  border-style: none;
  font-size: 20px;
  background-color: #f5f4f1;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 8px;
  transition: all .3s;
}

.btn_menu:active {
  background-color: #dadad5;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
}

.filter {
  background-color: #f1f0e8;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 8px;
}

.filter-title {
  margin: 0;
  width: 100%;
  font-size: 20px;
  padding: 5px 10px;
  border-top-left-radius: 8px;
  border-top-right-radius: 8px;
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