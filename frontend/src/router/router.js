import GeneralPage from "@/components/pages/GeneralPage";
import MyProduct from "@/components/pages/MyProduct";
import MyCategory from "@/components/pages/MyCategory";
import MyProfile from "@/components/pages/MyProfile";
import {createRouter, createWebHistory} from "vue-router";

const routes = [
    {
      path: '/',
      component: GeneralPage
    },
    {
        path: '/product',
        component: MyProduct
    },
    {
        path: '/category',
        component: MyCategory
    },
    {
        path: '/profile',
        component: MyProfile
    },

]


const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;