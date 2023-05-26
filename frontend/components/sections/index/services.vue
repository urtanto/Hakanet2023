<template>
  <hack-section v-if="services.length">
    <hack-content class="flex flex-col gap-10 justify-center flex-wrap">
      <h2 class="text-3xl text-center">Услуги</h2>
      <ul class="grid md:grid-cols-2 lg:grid-cols-3 mx-auto md:gap-12 gap-5">
        <li
          v-for="service in services"
          :key="service.id"
        >
          <hack-commerce-card
            :name="service.name"
            :description="service.description"
            :price="service.cost"
            class="h-full"
          />
        </li>
      </ul>
    </hack-content>
  </hack-section>
</template>

<script setup lang="ts">
import HackSection from "~/components/UI/HackSection.vue"
const config = useRuntimeConfig()
const { services } = await $fetch(`${config.public.apiUrl}/get/services`)
</script>
