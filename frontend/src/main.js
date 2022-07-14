import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios"
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.bundle'


axios.defaults.baseURL = 'http://fefumarket.ru:8000'


createApp(App).use(store).use(router, axios).mount('#app')
