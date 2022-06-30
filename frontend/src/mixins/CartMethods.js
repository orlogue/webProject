import {toast} from "bulma-toast";

export default {
    name: 'CartMethods',
    data() {
        return {
            cart: {
                items: [],
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        addToCart(product) {
            const item = {
                product: product,
                quantity: 1
            }
            this.$store.commit('addToCart', item)
            toast({
                message: 'Товар был добавлен в корзину!',
                type: 'is-success',
                dismissible: false,
                pauseOnHover: true,
                duration: 2500,
                position: 'bottom-right',
            })
        },
        checkPresenceInCart(product) {
            const exists = this.cart.items.filter(item => item.product.id === product.id)
            return !exists.length
        },
        removeFromCart(product) {
            this.$store.commit('removeFromCart', product)
            toast({
                message: 'Товар был удалён из корзины!',
                type: 'is-success',
                dismissible: false,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
    }
}