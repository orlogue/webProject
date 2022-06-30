import {createStore} from 'vuex'

export default createStore({
    state: {
        cart: {
            items: [],
        },
        isAuthenticated: false,
        token: '',
        isLoading: false
    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('cart')) {
                state.cart = JSON.parse(localStorage.getItem('cart'))
            } else {
                localStorage.setItem('cart', JSON.stringify(state.cart))
            }

            if (localStorage.getItem('token')) {
                state.token = localStorage.getItem('token')
                state.isAuthenticated = true
            } else {
                state.token = ''
                state.isAuthenticated = false
            }
        },
        addToCart(state, item) {
            const exists = state.cart.items.filter(i => i.product.id === item.product.id)
            if (exists.length) {
                exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
            } else {
                state.cart.items.push(item)
            }
            localStorage.setItem('cart', JSON.stringify(state.cart))
        },
        changeQuantity(state, item) {
            const foundItem = state.cart.items.filter(i => i.product.id === item.product.id)
            foundItem[0].quantity = parseInt(item.quantity)
            // state.cart.items[index].quantity = parseInt(quantity)
            localStorage.setItem('cart', JSON.stringify(state.cart))
        },
        removeFromCart(state, product) {
            state.cart.items = state.cart.items.filter(i => i.product.id !== product.id)
            localStorage.setItem('cart', JSON.stringify(state.cart))
        },
        clearCart(state) {
            state.cart = {items: []}
            localStorage.setItem('cart', JSON.stringify(state.cart))
        },
        setIsLoading(state, status) {
            state.isLoading = status
        },
        setToken(state, token) {
            state.token = token
            state.isAuthenticated = true
        },
        removeToken(state) {
            state.token = ''
            state.isAuthenticated = false
        },
    },
    actions: {},
    modules: {}
})