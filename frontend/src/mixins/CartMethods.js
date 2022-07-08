export default {
    name: 'CartMethods',
    data() {
        return {}
    },
    methods: {
        addToCart(product) {
            const item = {
                product: product,
                quantity: 1
            }
            this.$store.commit('addToCart', item)
        },
        checkPresenceInCart(product) {
            const exists = this.$root.cart.items.filter(item => item.product.id === product.id)
            return !exists.length
        },
        checkProductSeller(id) {
            if (id === this.$root.profile.id)
                return 1
            else
                return 0
        },
        removeFromCart(product) {
            this.$store.commit('removeFromCart', product)
        }
    }
}