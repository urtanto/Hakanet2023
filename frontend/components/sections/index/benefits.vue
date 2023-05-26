<template>
  <hack-section>
    <hack-content class="flex flex-col gap-10 justify-center">
      <h2 class="text-center text-3xl">Наши преимущества</h2>
      <ul class="grid md:grid-cols-2 lg:grid-cols-3 mx-auto md:gap-12 gap-5">
        <li class="max-w-sm p-6 bg-accent rounded-xl flex justify-center items-center flex-col gap-3 shadow">
          <svg
            fill="none"
            class="w-10 h-10 text-default"
            stroke="currentColor"
            stroke-width="1.5"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M21 7.5l-2.25-1.313M21 7.5v2.25m0-2.25l-2.25 1.313M3 7.5l2.25-1.313M3 7.5l2.25 1.313M3 7.5v2.25m9 3l2.25-1.313M12 12.75l-2.25-1.313M12 12.75V15m0 6.75l2.25-1.313M12 21.75V19.5m0 2.25l-2.25-1.313m0-16.875L12 2.25l2.25 1.313M21 14.25v2.25l-2.25 1.313m-13.5 0L3 16.5v-2.25"
            ></path>
          </svg>
          <h3 class="text-base text-center text-default">Максимальная защита ваших вещей от повреждений при чистке</h3>
        </li>
        <li class="max-w-sm p-6 bg-accent rounded-xl flex justify-center items-center flex-col gap-3 shadow">
          <svg
            class="w-10 h-10 text-default"
            fill="none"
            stroke="currentColor"
            stroke-width="1.5"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z"
            ></path>
          </svg>
          <h3 class="text-base text-center text-default">
            Использование только высококачественных моющих и кондиционирующих средств
          </h3>
        </li>
        <li class="max-w-sm p-6 bg-accent rounded-xl flex justify-center items-center flex-col gap-3 shadow">
          <svg
            fill="none"
            class="w-10 h-10 text-default"
            stroke="currentColor"
            stroke-width="1.5"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M8.25 18.75a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m3 0h6m-9 0H3.375a1.125 1.125 0 01-1.125-1.125V14.25m17.25 4.5a1.5 1.5 0 01-3 0m3 0a1.5 1.5 0 00-3 0m3 0h1.125c.621 0 1.129-.504 1.09-1.124a17.902 17.902 0 00-3.213-9.193 2.056 2.056 0 00-1.58-.86H14.25M16.5 18.75h-2.25m0-11.177v-.958c0-.568-.422-1.048-.987-1.106a48.554 48.554 0 00-10.026 0 1.106 1.106 0 00-.987 1.106v7.635m12-6.677v6.677m0 4.5v-4.5m0 0h-12"
            ></path>
          </svg>
          <h3 class="text-base text-center text-default">
            Для удобства клиентов мы предоставляем услуги забора и доставки вещей на дом.
          </h3>
        </li>
      </ul>
    </hack-content>
  </hack-section>
</template>

<script setup lang="ts">
import HackSection from "~/components/UI/HackSection.vue"
</script>
