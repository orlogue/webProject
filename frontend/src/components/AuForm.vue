<template>
  <div class="authorization">
    <div class="">
      <div class="">
        <h1 class="">Авторизация</h1>

        <form @submit.prevent="submitForm">
          <div class="input1">
          <div class="">
            <label>Номер телефона</label>
            <div class="phone">
              <input type="text" class="" v-model="phone_number">
            </div>
          </div>

          <div class="">
            <label>Пароль</label>
            <div class="">
              <input type="password" class="" v-model="password">
            </div>
          </div>
      </div>
          <div class="error" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>

          <div class="">
            <div class="">
              <br>
              <button class="btn_aut">Войти</button>
            </div>
          </div>

        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'LogIn',
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Log In | Djackets'
  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = ""
      localStorage.removeItem("token")
      const formData = {
        phone_number: this.phone_number,
        password: this.password
      }
      await axios
          .post("/api/v1/token/login/", formData)
          .then(response => {
            const token = response.data.auth_token
            this.$store.commit('setToken', token)

            axios.defaults.headers.common["Authorization"] = "Token " + token
            localStorage.setItem("token", token)
            const toPath = this.$route.query.to || '/cart'
            this.$router.push(toPath)
          })
          .catch(error => {
              this.errors.push('Что-то пошло не так.')
              this.errors.push('Попробуйте снова!')
              console.log(JSON.stringify(error))

          })
    }
  }
}
</script>

<style>
.btn_aut {
  background-color: #81b29a;
  font-size: 20px;
  padding: 5px;
  margin-left: 65px;
  border-radius: 4px;
  border: 1px ;
  color: #f4f1de;
  transition: all .4s;
}
.btn_aut:hover {
  box-shadow: 0 0 10px rgba(0,0,0,0.4);
}
.phone {
  margin-bottom: 10px;
  height: 25px;
  width: 170px;
}
.authorization {
  margin: 20px 50px 50px 50px;
  padding: 0;
}
input {
  margin-bottom: 10px;
  height: 25px;
}
.input1 {
  margin-left: 15px;
  font-size: 20px;
}
.error {
  margin-left: 25px;
  margin-bottom: -15px;
  color: red;
}
</style>