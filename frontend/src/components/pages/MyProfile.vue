<template>
  <nav-bar>
  </nav-bar>
  <div class="container">
    <div class="row mt-2">
      <div class="col cols-4 d-flex flex-column">
        <div class="card fs-5">
          <div class="card-header ps-3 py-2 d-flex align-items-center">
            <h2 style="margin-bottom: 0;">
            </h2>
            <a class="btn btn-sm btn-secondary ms-auto" href="">Редактировать</a>
          </div>
          <div class="row px-3">
            <div class="col col-lg-2 col-sm-3 p-0 flex-fill">
              <span class="list-group-item">Имя: {{ profile.name }}</span>
            </div>
          </div>
          <div class="row px-3">
            <div class="col col-lg-2 col-sm-3 p-0 flex-fill">
              <span class="list-group-item">Номер телефона: {{ profile.phone_number }}</span>
            </div>
          </div>
          <div class="row px-3">
            <div class="col col-lg-2 col-sm-3 p-0 flex-fill">
              <span class="list-group-item">Корпуc: {{ profile.building }}</span>
            </div>
          </div>
          <div class="row px-3">
            <div class="col col-lg-2 col-sm-3 p-0 flex-fill">
              <span class="list-group-item">Комната: {{ profile.room }}</span>
            </div>
          </div>
        </div>
      </div>
      <div class="col col-lg-8 d-flex flex-column">
        <div class="card fs-5">
          <div class="card-header ps-3 py-2">
            <h2 style="margin-bottom: 0;">
              История заказов
            </h2>
          </div>
          <div class="row px-3">
            <div class="col col-lg-2 col-sm-3 p-0 flex-fill">
              <span class="list-group-item">Заказ</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <my-footer></my-footer>
</template>

<script>

import NavBar from "@/components/NavBar";
import MyFooter from "@/components/UI/MyFooter";
import API from "@/mixins/API";
import axios from "axios";

export default {
  components: {NavBar, MyFooter},
  mixins: [API],
  data() {
    return {
      profile: {},
      dialogVisible: true,
    }
  },
  mounted() {
    this.getProfile()
  },
  methods: {
    showDialog() {
      this.dialogVisible = true;
    },
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
</style>