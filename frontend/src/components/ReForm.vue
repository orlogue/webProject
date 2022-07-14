<template>
  <div v-if="singUpContent" class="registration">
    <h1 class="mb-4 text-center">Регистрация</h1>
    <form class="d-flex flex-column justify-content-center" @submit.prevent="submitForm">
      <div class="fs-5 mb-2">
        <label>Номер телефона</label>
        <div class="flex-fill">
          <input type="text" class="form-input-reg" v-model="phone_number">
        </div>
      </div>
      <div class="fs-5 mb-2">
        <label>Имя</label>
        <div class="flex-fill">
          <input type="text" class="form-input-reg" v-model="name">
        </div>
      </div>
      <div class="fs-5 mb-2">
        <label>Корпус</label>
        <div class="flex-fill">
          <select class="building" @change="setBuilding($event)">
            <option selected disabled>Выберите корпус</option>
            <option v-for="building in buildings"
                    :key="building.id"
                    :value="building.name"
            >{{ building.name }}
            </option>
          </select>
        </div>
      </div>
      <div class="fs-5 mb-2">
        <label>Комната</label>
        <div class="flex-fill">
          <input type="text" class="form-input-reg" v-model="room">
        </div>
      </div>
      <div class="fs-5 mb-2">
        <label>Пароль</label>
        <div class="flex-fill">
          <input type="password" class="form-input-reg" v-model="password">
        </div>
      </div>

      <div class="fs-5 mb-2">
        <label>Подтверждение</label>
        <div class="">
          <input type="password" class="form-input-reg" v-model="password2">
        </div>
      </div>
      <p class="error mb-0" v-if="error">{{ error }}</p>
      <button class="btn_aut mt-4">Зарегистрироваться</button>
    </form>
  </div>
  <div v-else class="registration-final">
    <div class="d-flex flex-column justify-content-center">
      <h3 class="mb-4 text-center">Завершение регистрации</h3>
      <p class="fs-5">Для полной работы сайта необходимо перейти в телеграм-бота
        и cледовать инструкции.</p>
      <p class="fs-5"> Тг-бот нужен для подтверждения продажи продавцом
        и получения уведомления о покупке.
      </p>
      <a href="https://t.me/fefumarket_bot"
         target="_blank"
         class="mt-2 mx-auto"
         @click="this.$router.push({name: 'Products'})"
      >
        <button class="btn_aut"
        >Телеграм-бот
        </button>
      </a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import API from "@/mixins/API";

export default {

  name: 'SignUp',
  data() {
    return {
      buildings: [],
      phone_number: '',
      name: '',
      building: '',
      room: '',
      password: '',
      password2: '',
      error: '',
      singUpContent: true
    }
  },
  mixins: [API],
  mounted() {
    this.getBuildings()
  },
  methods: {
    setBuilding(e) {
      this.building = e.target.value
    },
    async submitForm() {
      this.errors = []
      if (this.phone_number === '' || this.name === '' || this.building === '' || this.room === '' || this.password === '') {
        this.error = 'Введите все данные!'
        return 0;
      }

      if (!this.errors.length) {
        const formData = {
          phone_number: this.phone_number,
          name: this.name,
          building: this.building,
          room: this.room,
          password: this.password
        }
        await axios
            .post("/api/users/", formData)
            .then(response => {
            })
            .catch(error => {
              if (error.response) {
                this.error = ('Что-то пошло не так.\nПопробуйте снова!')
              }
            })
        await axios
            .post('/auth/token/login/', {
              phone_number: formData['phone_number'],
              password: formData['password']
            })
            .then(response => {
              const token = response.data.auth_token
              this.$store.commit('setToken', token)

              axios.defaults.headers.common["Authorization"] = "Token " + token
              localStorage.setItem("token", token)
            })
        this.singUpContent = false
      }
    }
  }
}
</script>

<style scoped>
.registration {
  max-width: 256px;
  margin: 10px 40px;
  padding: 0;
}

.registration-final {
  max-width: 340px;
  margin: 10px 40px;
  padding: 0;
}

.building {
  height: 30px;
  border-style: none;
  align-self: flex-end;
  width: 100%;
  padding: 0 6px;
  margin: 0 0 10px 0;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
  border-radius: 8px;
}

.btn_reg {
  background-color: #81b29a;
  font-size: 20px;
  padding: 5px;
  margin-left: -10px;
  border-radius: 4px;
  border: 1px;
  color: #f4f1de;
  transition: all .4s;
}

.btn_reg:hover {
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.4);
}

.form-input-reg {
  width: 100%;
  border-radius: 8px;
  margin-bottom: 10px;
  height: 30px;
}

select {
  font-size: 18px;
  width: 170px;
  border: 1px solid #000000;

  border-radius: 4px;
  height: 29px;
}
</style>