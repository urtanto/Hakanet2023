<template>
  <div>
    <h1>Home</h1>
    <p>
      Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit itaque excepturi atque aliquam distinctio dolore,
      repudiandae voluptatibus officiis quo molestiae!
    </p>
    <p>
      Lorem ipsum dolor, sit amet consectetur adipisicing elit. Fugit itaque excepturi atque aliquam distinctio dolore,
      repudiandae voluptatibus officiis quo molestiae!
    </p>
  </div>
</template>

<script lang="ts" setup>
import { onMounted } from "vue"
import { initModals, initCollapses } from "flowbite"
definePageMeta({
  title: "Home",
  description: "Home page of Nuxt Site",
})

onMounted(() => {
  initModals()
  initCollapses()
})
</script>
