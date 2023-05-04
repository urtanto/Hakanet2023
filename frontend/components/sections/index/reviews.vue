<template>
  <section class="flex flex-col gap-10 justify-center flex-wrap mb-10">
    <h2 class="text-center text-3xl">Отзывы</h2>
    <div class="rounded-lg grid grid-cols-2 gap-5 grid-rows-auto">
      <div
        class="items-center relative rounded-lg flex bg-accent"
        v-for="review in reviews"
        :key="review.id"
      >
        <span
          class="absolute inline-block right-5 rotate-180 w-6 h-6 top-6 z-[2] opacity-50 text-accent-400 text-2xl font-bold"
        >
          <svg
            fill="currentColor"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink"
            viewBox="0 0 46.195 46.195"
            xml:space="preserve"
          >
            <g
              id="SVGRepo_bgCarrier"
              stroke-width="0"
            ></g>
            <g
              id="SVGRepo_tracerCarrier"
              stroke-linecap="round"
              stroke-linejoin="round"
            ></g>
            <g id="SVGRepo_iconCarrier">
              <g>
                <path
                  d="M35.765,8.264c-5.898,0-10.555,4.782-10.555,10.68s4.844,10.68,10.742,10.68 c0.059,0,0.148-0.008,0.207-0.009c-2.332,1.857-5.261,2.976-8.467,2.976c-1.475,0-2.662,1.196-2.662,2.67s0.949,2.67,2.424,2.67 c10.469-0.001,18.741-8.518,18.741-18.987c0-0.002,0-0.004,0-0.007C46.195,13.042,41.661,8.264,35.765,8.264z"
                ></path>
                <path
                  d="M10.75,8.264c-5.898,0-10.563,4.782-10.563,10.68s4.84,10.68,10.739,10.68 c0.059,0,0.146-0.008,0.205-0.009c-2.332,1.857-5.262,2.976-8.468,2.976C1.188,32.591,0,33.787,0,35.261s0.964,2.67,2.439,2.67 c10.469-0.001,18.756-8.518,18.756-18.987c0-0.002,0-0.004,0-0.007C21.195,13.042,16.646,8.264,10.75,8.264z"
                ></path>
              </g>
            </g>
          </svg>
        </span>
        <img
          class="rounded-s-lg h-full"
          :src="review.author_img"
          :alt="review.author"
        />
        <div class="p-2 flex flex-col gap-2">
          <h3 class="text-xl font-bold tracking-tight text-default">
            <a href="#">{{ review.author }}</a>
          </h3>
          <p class="font-light text-default">
            {{ review.msg }}
          </p>
        </div>
      </div>
    </div>
  </section>
</template>

<style scoped>
.grid-rows-auto {
  grid-auto-rows: 16rem;
}
</style>

<script setup lang="ts">
interface Review extends Object {
  id: number
  author: string
  msg: string
  author_img: string
}
const reviews: Review[] = [
  { id: 0, author: "Какой-то нн", msg: "Зажопили норм сайт, засранцы", author_img: "https://i.pravatar.cc/1000" },
  { id: 1, author: "Какой-то нн", msg: "Зажопили норм сайт, засранцы", author_img: "https://i.pravatar.cc/1000" },
  { id: 1, author: "Какой-то нн", msg: "Зажопили норм сайт, засранцы", author_img: "https://i.pravatar.cc/1000" },
]
</script>
