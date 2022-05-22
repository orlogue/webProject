<template>
  <div class="registration">
    <div class="">
      <div class="">
        <h1 class="">Регистрация</h1>

        <form @submit.prevent="submitForm">
          <div class="input">
          <div class="">
            <label>Номер телефона</label>
            <div class="">
              <input type="text" class="" v-model="phone_number">
            </div>
          </div>

          <div class="">
            <label>Имя</label>
            <div class="">
              <input type="text" class="" v-model="name">
            </div>
          </div>

          <div class="">
            <label>Корпус</label>
            <div class="">
              <select class="build" v-model="building">>
                <option></option>
                <option>7.2</option>
                <option>6.2</option>
                <option>6.1</option>
                <option>8.2</option>
                <option>7.1</option>
                <option>8.1</option>
              </select>
            </div>
          </div>

          <div class="">
            <label>Комната</label>
            <div class="">
              <input type="text" class="" v-model="room">
            </div>
          </div>

          <div class="">
            <label>Пароль</label>
            <div class="">
              <input type="password" class="" v-model="password">
            </div>
          </div>

          <div class="">
            <label>Повторите пароль</label>
            <div class="">
              <input type="password" class="" v-model="password2">
            </div>
          </div>

          <div class="error1" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>

          <div class="">
            <div class="">
              <br>
              <button class="btn_reg">Зарегистрироваться</button>
            </div>
          </div>
          </div>
        </form>

      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'


export default {

  name: 'SignUp',
  data() {
    return {
      phone_number: '',
      name: '',
      building: '',
      room: '',
      password: '',
      password2: '',
      errors: []
    }
  },
  methods: {
    submitForm() {
      this.errors = []
      if (this.phone_number === '' || this.name === '' || this.building === ''|| this.room === '' || this.password === '' ) {
        this.errors.push('Введите все данные')
      }

      if (!this.errors.length) {
        const formData = {
          phone_number: this.phone_number,
          name: this.name,
          builting: this.building,
          room: this.room,
          password: this.password
        }
        axios
            .post("/api/v1/users/", formData)
            .then(() => {
              toast({
                message: 'Account created, please log in!',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
              })
              this.$router.push('/log-in')
            })
            .catch(error => {
              if (error.response) {
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }
                console.log(JSON.stringify(error.response.data))
              } else if (error.message) {
                this.errors.push('Something went wrong. Please try again')

                console.log(JSON.stringify(error))
              }
            })
      }
    }
  }
}
</script>

<style>
.registration {
  margin: 20px 50px 50px 50px;
  padding: 0;
}
.btn_reg {
  background-color: #81b29a;
  font-size: 20px;
  padding: 5px;
  margin-left: -10px;
  border-radius: 4px;
  border: 1px ;
  color: #f4f1de;
  transition: all .4s;
}
.btn_reg:hover {
  box-shadow: 0 0 10px rgba(0,0,0,0.4);
}
input {
  border-radius: 4px;
  border: 1px solid #000000;
  margin-bottom: 10px;
  height: 25px;

}
.input {
  margin-left: 18px;
  font-size: 20px;
}
select {
  font-size: 18px;
  width: 170px;
  border: 1px solid #000000;

  border-radius: 4px;
  height: 29px;
}
.error1 {
  color: #ff0000 ;
}
</style>