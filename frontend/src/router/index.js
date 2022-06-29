import GeneralPage from "@/components/pages/GeneralPage";
import { createRouter, createWebHistory } from 'vue-router'

import MyProduct from "@/components/pages/MyProduct";
import MyCategory from "@/components/pages/MyCategory";
import MyProfile from "@/components/pages/MyProfile";
import NotFound from "@/components/pages/404";

const routes = [
    {
        path: '/',
        component: GeneralPage,
        name: 'Home',
    },
    {
        path: '/products',
        component: MyProduct,
        name: 'Products'
    },
    {
        path: '/category',
        component: MyCategory,
        name: 'Category',
        // beforeEnter: (to, from, next) => {
        //     if (localStorage.getItem('token')) {
        //         next()
        //     } else {
        //         next({ name: 'Home' })
        //     }
        // }
    },
    {
        path: '/category/:slug/',
        component: () => import('@/components/pages/MyCategory')
    },
    {
        path: '/category/:slug1/:slug2/',
        component: () => import('@/components/pages/MyCategory')
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
        next({ name: 'Home' })
    }
})

export default router;

