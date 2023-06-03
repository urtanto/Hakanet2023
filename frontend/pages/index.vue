<template>
  <hero />
  <benefits />
  <services />
  <reviews />
</template>

<script lang="ts" setup>
import { onMounted } from "vue"
import hero from "~/components/sections/index/hero.vue"
import benefits from "~/components/sections/index/benefits.vue"
import services from "~/components/sections/index/services.vue"
import reviews from "~/components/sections/index/reviews.vue"


import { initModals, initCollapses, initCarousels } from "flowbite"
definePageMeta({
  title: "Home",
  description: "Home page of Nuxt Site",
})
onMounted(() => {
  initModals()
  initCollapses()
  initCarousels()
})
</script>
