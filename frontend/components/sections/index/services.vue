<template>
    <section v-if="services.length" class="flex flex-col gap-10 justify-center flex-wrap mb-10">
      <h2 class="text-3xl text-center">Услуги</h2>
    <ul class="grid grid-cols-3 auto-rows-fr gap-5">
      <li  v-for="service in services" :key="service.id">
        <hack-commerce-card :name="service.name" :description="service.description" :price="service.cost" class="h-full"/>
          </li>
    </ul>
  </section>
</template>

<script setup lang="ts">
  const {services} = await $fetch('https://api.stylelifeweb.su/get/services/')
</script>
