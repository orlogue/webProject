import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from "axios"
// import BootstrapVue from 'bootstrap-vue/dist/bootstrap-vue.esm';

import 'bootstrap-vue/dist/bootstrap-vue.css';
import 'bootstrap/dist/css/bootstrap.css';

// createApp.use(BootstrapVue);


axios.defaults.baseURL = 'http://127.0.0.1:8000'



createApp(App).use(store).use(router, axios).mount('#app')
