<template>
  <ul
    class="flex flex-col p-4 md:p-0 mt-4 font-medium border border-gray-100 rounded-lg bg-gray-50 md:flex-row md:space-x-8 md:mt-0 md:border-0 md:bg-transparent"
  >
    <li
      v-for="page in pages"
      :key="page.slug.value"
      class="text-white"
    >
      <hack-link
        :to="page.slug.value"
        aria-current="page"
        >{{ page.title.value }}</hack-link
      >
    </li>
  </ul>
</template>

<script setup lang="ts">
import { PropType, Ref } from "vue"

interface Page extends Object {
  slug: Ref<String>
  title: Ref<String>
}
defineProps({
  pages: Array as PropType<Page[]>,
})
</script>
