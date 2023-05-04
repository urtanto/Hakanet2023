<template>
  <section class="h-screen w-full z-[1] mb-10">
    <div class="absolute top-0 bottom-0 left-0 right-0">
      <div class="absolute w-full h-full bg-accent opacity-50 z-[2]"></div>
      <div
        class="w-full h-full z-[1] bg-cover bg-no-repeat bg-fixed bg-center bg-[url(~/assets/images/banners/hero.jpg)]"
      ></div>
    </div>
    <div class="flex justify-center gap-10 align-center relative z-10 w-full h-full">
      <logo
        class="h-full"
        alt="Shoe Way Logo"
      />
      <div class="flex-col flex gap-3 justify-center">
        <h1 class="text-5xl text-default">Надежная и&nbsp;профессиональная очистка сумок и&nbsp;кроссовок!</h1>
        <p class="text-medium text-default">
          Наша компания предоставлят лучший способ продлить жизнь вашей обуви и сохранить идеальный внешний вид аксессуаров.
          Узнайте, как мы используем передовые технологии и&nbsp;материалы для тщательной очистки каждой пары обуви и сумочки,
          и&nbsp;наслаждайтесь абсолютной чистотой и свежестью каждый день!
        </p>
      </div>
    </div>
  </section>
</template>

<script setup lang="ts">
import logo from "~/assets/images/logo.svg"
</script>
