import GeneralPage from "@/components/pages/GeneralPage";
import {createRouter, createWebHistory} from 'vue-router'

import ProductsList from "@/components/pages/ProductsList";
import MyProfile from "@/components/pages/MyProfile";
import NotFound from "@/components/pages/404";
import ProductDetail from "@/components/pages/ProductDetail";

const routes = [
    {
        path: '/',
        component: GeneralPage,
        name: 'Home',
    },
    {
        path: '/products',
        component: ProductsList,
        name: 'Products'
    },
    {
        path: '/products/:slug',
        component: ProductDetail,
        name: 'ProductDetail'
    },
    {
        path: '/profile',
        component: MyProfile
    },
    {
        path: '/:catchAll(.*)',
        component: NotFound
    }

]


const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

router.beforeEach((to, from, next) => {
    if (localStorage.getItem('token')) {
        next()
    } else if (to.path === '/') {
        next()
    } else {
        next({name: 'Home'})
    }
})

export default router;

