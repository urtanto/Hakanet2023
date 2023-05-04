<template>
  <div class="max-w-sm p-4 bg-accent rounded-xl flex justify-center items-center flex-col gap-3 shadow">
    <h3 class="text-2xl text-center text-default">{{ name }}</h3>
    <p class="text-base text-default">{{ description }}</p>
    <div class="flex items-center w-full justify-between">
      <hack-button
        href="#"
        typeBtn="solid"
      >
        Подробнее
      </hack-button>
      <span class="text-3xl font-bold text-gray-900 dark:text-white">{{ price }}₽</span>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps({
  price: {
    type: Number,
  },
  name: {
    type: String,
  },
  description: {
    type: String,
  },
})
</script>
