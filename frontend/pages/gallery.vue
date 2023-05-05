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



const filterPhotos = (filterOptions) => photos.filter(el => (filterOptions.type.includes(el.type) && filterOptions.material.includes(el.material)))


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
    <div class="relative overflow-hidden rounded-lg md:h-96 mt-24">
      <div
        class="hidden flex duration-700 ease-in-out place-content-center"
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
    <div class="flex justify-center pt-4">
      <button
        type="button"
        class="flex mr-2 h-full cursor-pointer group focus:outline-none"
        data-carousel-prev
      >
        <span class="text-gray-400 hover:text-accent-400 dark:hover:text-white">
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
        class="flex h-full cursor-pointer group focus:outline-none"
        data-carousel-next
      >
        <span class="text-gray-400 hover:text-accent-400 dark:hover:text-white">
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
      <button
        type="button"
        class="flex ml-10 items-center h-full cursor-pointer group focus:outline-none"
        data-modal-toggle
      >
        <span class="text-gray-400 hover:text-accent-400 dark:hover:text-white">
          <svg
            aria-hidden="true"
            class="w-6 h-6"
            fill="currentColor"
            viewBox="0 0 500 500"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              fill-rule="evenodd"
              d="M440.813 280.5c0-7.65 2.55-15.3 2.55-25.5s0-17.85-2.55-25.5l53.55-43.35c5.1-5.1 5.1-10.2 2.55-15.3l-51-89.25c-2.55-2.55-7.649-5.1-15.3-2.55l-63.75 25.5c-12.75-10.2-28.05-17.85-43.35-25.5l-10.2-66.3C315.863 5.1 308.212 0 303.113 0h-102c-5.101 0-12.75 5.1-12.75 10.2l-10.2 68.85c-15.3 5.1-28.05 15.3-43.35 25.5l-61.2-25.5c-7.65-2.55-12.75 0-17.851 5.1l-51 89.25c-2.55 2.55 0 10.2 5.1 15.3l53.55 40.8c0 7.65-2.55 15.3-2.55 25.5s0 17.85 2.55 25.5l-53.55 43.35c-5.1 5.101-5.1 10.2-2.55 15.301l51 89.25c2.55 2.55 7.649 5.1 15.3 2.55l63.75-25.5c12.75 10.2 28.05 17.85 43.35 25.5l10.2 66.3c0 5.1 5.1 10.2 12.75 10.2h102c5.101 0 12.75-5.101 12.75-10.2l10.2-66.3c15.3-7.65 30.6-15.3 43.35-25.5l63.75 25.5c5.101 2.55 12.75 0 15.301-5.101l51-89.25c2.55-5.1 2.55-12.75-2.551-15.3l-58.649-40.8zm-188.7 63.75c-48.45 0-89.25-40.8-89.25-89.25s40.8-89.25 89.25-89.25 89.25 40.8 89.25 89.25-40.8 89.25-89.25 89.25z"
              clip-rule="evenodd"
            ></path>
          </svg>
          <span class="sr-only">Next</span>
        </span>
      </button>
    </div>
  </div>
</template>
