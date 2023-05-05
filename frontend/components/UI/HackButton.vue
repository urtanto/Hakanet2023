<template>
  <button
    type="button"
    :class="typeBtn === 'solid' ? solidStyles : typeBtn === 'outline' ? outlineStyles : ''"
  >
    <slot></slot>
  </button>
</template>

<script setup lang="ts">
defineProps({
  typeBtn: String,
})
const solidStyles =
  "text-accent-dark bg-default hover:bg-default-dark hover:border-default-dark border-2 border-default focus:outline-none font-medium rounded-full text-sm px-5 py-2.5 text-center"
const outlineStyles =
  "text-default border border-accent-500 hover:bg-accent-500 font-medium rounded-full text-sm px-5 py-2.5 text-center"
</script>
