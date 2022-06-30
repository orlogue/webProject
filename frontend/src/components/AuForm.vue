<template>
  <div class="authorization">
    <h1 class="mb-3 text-center">Авторизация</h1>
    <form @submit.prevent="submitForm">
      <div class="d-flex flex-column">
        <div class="fs-4 my-2">
          <label>Номер телефона</label>
          <div class="flex-fill">
            <input type="text" class="form-input" v-model="phone_number">
          </div>
        </div>
        <div class="fs-4">
          <label>Пароль</label>
          <input type="password" class="form-input" v-model="password">
        </div>
        <p class="error m-0" v-if="error">{{ error }}</p>
        <button class="btn_aut mt-4">Войти</button>
      </div>

      <!--      <div class="d-flex flex-column">-->
      <!--        <div class="flex-grow-1"><p class="error" v-if="error">{{ error }}</p></div>-->
      <!--        <button class="btn_aut align-self-center">Войти</button>-->
      <!--      </div>-->
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LogIn',
  data() {
    return {
      phone_number: '',
      password: '',
      error: '',
    }
  },
  methods: {
    async submitForm() {
      if (this.phone_number === '' || this.password === '') {
        this.error = 'Введите все данные!'
        return 0;
      }

      axios.defaults.headers.common["Authorization"] = ""
      localStorage.removeItem("token")
      const formData = {
        phone_number: this.phone_number,
        password: this.password
      }
      await axios
          .post("/auth/token/login/", formData)
          .then(response => {
            const token = response.data.auth_token
            this.$store.commit('setToken', token)

            axios.defaults.headers.common["Authorization"] = "Token " + token
            localStorage.setItem("token", token)
            const toPath = this.$route.query.to || '/products'
            this.$router.push(toPath)
          })
          .catch(error => {
            if (error.response) {
              this.error = 'Неверный номер телефона или пароль. Попробуйте снова!'
            }
          })
    }
  }
}
</script>

<style scoped>
.authorization {
  max-width: 256px;
  /*min-height: 360px;*/
  margin: 10px 40px;
}

.form-input {
  height: 40px;
  width: 100%;
  border-radius: 8px;
  margin-bottom: 10px;
  border-style: none;
}

</style>