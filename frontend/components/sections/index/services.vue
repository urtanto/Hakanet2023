<template>
    <section class="flex flex-col gap-10 justify-center flex-wrap mb-10">
    <div class="flex gap-2 justify-between align-center">
      <h2 class="text-3xl">Услуги</h2>
      <hack-link
        class="text-xl !text-accent-600 underline hover:no-underline"
        to="/services"
        >Посмотреть все</hack-link
      >
    </div>
    <ul class="grid grid-cols-3 auto-rows-fr gap-5">
      <li  v-for="service in services" :key="service.id">
        <hack-commerce-card :name="service.name" :description="service.description" :price="service.cost" class="h-full"/>
          </li>
    </ul>
  </section>
</template>

<script setup lang="ts">
  const {services} = await $fetch('http://127.0.0.1:8000/get/services/')
</script>
