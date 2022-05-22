import GeneralPage from "@/components/GeneralPage";
import {createRouter, createWebHistory} from "vue-router";

const routes = [
    {
      path: '/',
      component: GeneralPage
    },
]


const router = createRouter({
    routes,
    history: createWebHistory(process.env.BASE_URL)
})

export default router;