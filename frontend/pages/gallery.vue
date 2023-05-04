<script lang="ts" setup>
import { initCarousels, initFlowbite, Carousel } from "flowbite"
import { definePageMeta } from "~~/.nuxt/imports"
const photos = [
  {
    id: 1,
    src1: "https://static.wixstatic.com/media/37dda4_e8a77d014bad4b30a2a8039d511a1e58~mv2.jpeg/v1/fit/w_239,h_239,q_90/37dda4_e8a77d014bad4b30a2a8039d511a1e58~mv2.jpeg",
    src2: "https://static.wixstatic.com/media/37dda4_6593ef8367794fef84cd336008c9a280~mv2.jpeg/v1/fit/w_239,h_239,q_90/37dda4_6593ef8367794fef84cd336008c9a280~mv2.jpeg",
    type: "boots",
    material: "leather",
  },
  {
    id: 2,
    src1: "https://static.wixstatic.com/media/37dda4_7478c9b11e514a44be5bfd9d9d11bf26~mv2.jpeg/v1/fit/w_239,h_239,q_90/37dda4_7478c9b11e514a44be5bfd9d9d11bf26~mv2.jpeg",
    src2: "https://static.wixstatic.com/media/37dda4_1e9063f7a4c7413f976dfa53039517b8~mv2.jpeg/v1/fit/w_239,h_239,q_90/37dda4_1e9063f7a4c7413f976dfa53039517b8~mv2.jpeg",
    type: "boots",
    material: "sintetic",
  },
  {
    id: 3,
    src1: "https://static.wixstatic.com/media/37dda4_b870bb35a307408cacc5b96a6b85df30~mv2.jpeg/v1/fit/w_239,h_239,q_90/37dda4_b870bb35a307408cacc5b96a6b85df30~mv2.jpeg",
    src2: "https://static.wixstatic.com/media/37dda4_c4c8dee8c03f4f2cbe98c23be4608f3b~mv2.jpeg/v1/fit/w_239,h_239,q_90/37dda4_c4c8dee8c03f4f2cbe98c23be4608f3b~mv2.jpeg",
    type: "bag",
    material: "leather",
  },
]

definePageMeta({
  title: "Gallery",
  description: "Our photo",
})
onMounted(() => {
  initCarousels()
})
</script>
<template>
  <div
    id="custom-controls-gallery"
    class="relative w-full"
    data-carousel="slide"
  >
    <div class="relative h-56 overflow-hidden rounded-lg md:h-96">
      <div
        class="hidden flex duration-700 ease-in-out"
        :data-carousel-item="photo.id === 1 ? 'active' : ''"
        v-for="photo in photos"
        :key="photo.id"
      >
        <img
          :src="photo.src1"
          alt="..."
        />
        <img
          :src="photo.src2"
          alt="..."
        />
      </div>
    </div>
    <div class="flex justify-center items-center pt-4">
      <button
        type="button"
        class="flex justify-center items-center mr-4 h-full cursor-pointer group focus:outline-none"
        data-carousel-prev
      >
        <span
          class="text-gray-400 hover:text-gray-900 dark:hover:text-white group-focus:text-gray-900 dark:group-focus:text-white"
        >
          <svg
            aria-hidden="true"
            class="w-6 h-6"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l2.293 2.293a1 1 0 010 1.414z"
              clip-rule="evenodd"
            ></path>
          </svg>
          <span class="sr-only">Previous</span>
        </span>
      </button>
      <button
        type="button"
        class="flex justify-center items-center h-full cursor-pointer group focus:outline-none"
        data-carousel-next
      >
        <span
          class="text-gray-400 hover:text-gray-900 dark:hover:text-white group-focus:text-gray-900 dark:group-focus:text-white"
        >
          <svg
            aria-hidden="true"
            class="w-6 h-6"
            fill="currentColor"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M12.293 5.293a1 1 0 011.414 0l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-2.293-2.293a1 1 0 010-1.414z"
              clip-rule="evenodd"
            ></path>
          </svg>
          <span class="sr-only">Next</span>
        </span>
      </button>
    </div>
  </div>
</template>
