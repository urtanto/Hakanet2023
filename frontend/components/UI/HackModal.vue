<template>
  <div
    :id="idModal"
    tabindex="-1"
    aria-hidden="true"
    class="fixed top-0 left-0 right-0 bottom-0 inset-0 z-50 hidden w-screen p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-screen"
    data-modal-backdrop="dynamic"
  >
    <div class="relative w-full max-w-2xl max-h-full">
      <!-- Modal content -->
      <div class="relative bg-accent-800 rounded-lg shadow">
        <!-- Modal header -->
        <div class="flex items-start justify-center p-4 border-b rounded-t">
          <h3 class="text-xl font-semibold text-default">{{ nameModal }}</h3>
          <button
            type="button"
            class="text-default bg-transparent hover:bg-accent hover:text-default rounded-lg text-sm p-1.5 ml-auto inline-flex items-center"
            :data-modal-hide="idModal"
          >
            <svg
              aria-hidden="true"
              class="w-5 h-5"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                fill-rule="evenodd"
                d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                clip-rule="evenodd"
              ></path>
            </svg>
            <span class="sr-only">Закрыть окно</span>
          </button>
        </div>
        <!-- Modal body -->
        <div class="p-6 space-y-6">
          <slot> </slot>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from "vue"
defineProps({
  idModal: {
    type: String,
    required: true,
  },
  nameModal: {
    type: String,
    required: true,
  },
})
onMounted(() => {})
</script>
