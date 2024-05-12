import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import PeopleView from '../views/PeopleView.vue'
import AddView from '../views/AddView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/people',
    name: 'people',
    component: PeopleView
  },
  {
    path: '/add',
    name: 'add',
    component: AddView
  },  
  {
    path: '/about',
    name: 'about',
    component: AboutView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
