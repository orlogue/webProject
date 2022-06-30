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
                .get('/api/category/subcategory/')
                .then(response => {
                    this.categories = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
    }
}