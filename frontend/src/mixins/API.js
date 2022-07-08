import axios from "axios";

export default {
    methods: {
        async getBuildings() {
            await axios
                .get('api/buildings/')
                .then(response => {
                    this.buildings = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async getCategories() {
            await axios
                .get('/api/category/')
                .then(response => {
                    this.categories = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        async getProfile() {
            await axios
                .get('/api/users/me/', localStorage.getItem('token'))
                .then(response => {
                    this.profile = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        }
    }
}