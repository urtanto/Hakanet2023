<template>
  <hack-section class="min-h-screen flex items-center justify-center w-full h-full z-[1]">
    <div class="absolute top-0 bottom-0 left-0 right-0">
      <div class="absolute w-full h-full bg-accent opacity-50 z-[2]"></div>
      <div
        class="w-full h-full z-[1] bg-cover bg-no-repeat bg-fixed bg-center bg-[url(~/assets/images/banners/hero.jpg)]"
      ></div>
    </div>
    <div class="relative z-10 w-full h-full">
      <hack-content class="h-full flex justify-center gap-2 md:gap-10 items-center flex-wrap lg:flex-nowrap">
        <logo
          class="w-44 lg:w-auto lg:h-full"
          alt="Shoe Way Logo"
        />
        <div class="flex-col flex gap-3 justify-center">
          <h1 class="text-default fluid-text-2xl-3xl">Надежная и&nbsp;профессиональная очистка сумок и&nbsp;кроссовок!</h1>
          <p class="fluid-text-sm-base text-default">
            Наша компания предоставлят лучший способ продлить жизнь вашей обуви и сохранить идеальный внешний вид аксессуаров.
            Узнайте, как мы используем передовые технологии и&nbsp;материалы для тщательной очистки каждой пары обуви и сумочки,
            и&nbsp;наслаждайтесь абсолютной чистотой и свежестью каждый день!
          </p>
        </div>
      </hack-content>
    </div>
  </hack-section>
</template>

<script setup lang="ts">
import logo from "~/assets/images/logo.svg"
import HackSection from "~/components/UI/HackSection.vue"
import HackContent from "~/components/UI/HackContent.vue"
</script>
