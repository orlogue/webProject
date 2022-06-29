<template>
  <div class="authorization">
        <h1 class="mb-4">Авторизация</h1>
        <form class="d-flex flex-column justify-content-center" @submit.prevent="submitForm">
            <div class="fs-4 my-2">
              <label>Номер телефона</label>
              <div class="flex-fill">
                <input type="text" class="inpt" v-model="phone_number">
              </div>
            </div>

            <div class="fs-4 my-2">
              <label>Пароль</label>
              <div class="">
                <input type="password" class="inpt" v-model="password">
              </div>
            </div>
          <div class="error" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>
          <button class="btn_aut mt-4 mx-auto">Войти</button>
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
          .post("/auth/token/login/", formData)
          .then(response => {
            const token = response.data.auth_token
            this.$store.commit('setToken', token)

            axios.defaults.headers.common["Authorization"] = "Token " + token
            localStorage.setItem("token", token)
            const toPath = this.$route.query.to || '/category'
            this.$router.push(toPath)
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
            } else {
              this.errors.push('Что-то пошло не так. Попробуйте снова!')

              console.log(JSON.stringify(error))
            }
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
  /*margin: 0 auto;*/
  border-radius: 4px;
  border: 1px ;
  color: #f4f1de;
  transition: all .4s;
}
.btn_aut:hover {
  box-shadow: 0 0 10px rgba(0,0,0,0.4);
}
/*.phone {*/
/*  margin-bottom: 10px;*/
/*  height: 25px;*/
/*  width: 170px;*/
/*}*/
.authorization {
  margin: 20px 50px 50px 50px;
  padding: 0;
}
.inpt {
  /*margin-bottom: 10px;*/
  height: 40px;
  border-radius: 8px;
}
/*.input1 {*/
/*  margin-left: 15px;*/
/*  font-size: 20px;*/
/*}*/
.error {
  margin-left: 25px;
  margin-bottom: -15px;
  color: red;
}
</style>