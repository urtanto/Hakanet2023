<template>
  <nav class="bg-accent fixed w-full z-50 top-0 left-0">
    <div
      class="max-w-screen-xl relative flex gap-y-3 items-center justify-between mx-auto p-4">
        <nuxt-link to="/" class="flex h-10 text-default">
          <logo class="h-full" />
        </nuxt-link>
      <div class="flex justify-end md:order-2 w-full md:w-auto">
        <div class="flex gap-1">
          <div class="flex gap-3" v-if="!authStore.auth.user">
          <hack-button typeBtn="solid" data-modal-target="registerModal" data-modal-toggle="registerModal">Регистрация</hack-button>
          <hack-button typeBtn="outline" data-modal-target="loginModal" data-modal-toggle="loginModal">Вход</hack-button>
          </div>
          <div v-else class="flex items-center justify-between gap-3">
            <p class="text-default text-2xl capitalize">{{useAuthStore().auth.user?.username}}</p>
            <hack-button type-btn="outline" @click="logout()">Выход</hack-button>
          </div>
        <button data-collapse-toggle="navbar-sticky" type="button"
          class="inline-flex items-center p-2 text-sm text-gray-500 rounded-lg md:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600"
          aria-controls="navbar-sticky" aria-expanded="false">
          <span class="sr-only">Открыть навигационное меню</span>
          <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
              d="M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z"
              clip-rule="evenodd"></path>
          </svg>
        </button>
          <hack-modal-register />
          <hack-modal-login />
        </div>
      </div>
      <div
        class="items-center justify-between top-28 sm:top-16 left-0 fixed md:static hidden w-full md:flex md:w-auto md:order-1"
        id="navbar-sticky">
        <HackNav :pages="pages"></HackNav>
      </div>
    </div>
  </nav>
</template>
<script lang="ts" setup>
import { initModals } from "flowbite";
import logo from "~/assets/images/smallLogo.svg"
const pages = [
  {
    title: ref("Главная"),
    slug: ref("/"),
  },
  {
    title: ref("О нас"),
    slug: ref("/about"),
  },
  {
    title: ref("Галлерея"),
    slug: ref("/gallery"),
  }
]
const authStore = useAuthStore()
const logout = async () => {
  await authStore.deleteAuthData();
  initModals()
}
</script>
<style scoped></style>
