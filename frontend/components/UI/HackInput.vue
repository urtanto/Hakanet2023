<template>
  <div class="w-full flex flex-col">
    <div class="flex gap-3 group relative z-0 w-full">
      <input
        :type="typeInput"
        :name="nameInput"
        :id="idInput"
        :value="modelValue"
        @input="updateInput"
        class="block py-2.5 px-0 w-full text-sm text-default bg-transparent border-0 border-b-2 border-default-dark appearance-none focus:outline-none focus:ring-0 focus:border-accent-500 peer"
        placeholder=" "
      />
      <label
        :for="idInput"
        class="peer-focus:font-medium absolute text-sm text-default duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:left-0 peer-focus:text-accent-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6"
      >
        <slot />
      </label>
      <button
        type="button"
        v-if="typeInput === 'password'"
        @click="$emit('changeMode', idInput)"
        class="text-default-dark border border-default-dark transition-all duration-150 hover:text-accent-500 hover:!border-accent-500 font-medium rounded-full text-sm p-2.5 text-center inline-flex items-center"
      >
        <svg
          v-if="!visible"
          aria-hidden="true"
          class="w-5 h-5"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            clip-rule="evenodd"
            fill-rule="evenodd"
            d="M3.28 2.22a.75.75 0 00-1.06 1.06l14.5 14.5a.75.75 0 101.06-1.06l-1.745-1.745a10.029 10.029 0 003.3-4.38 1.651 1.651 0 000-1.185A10.004 10.004 0 009.999 3a9.956 9.956 0 00-4.744 1.194L3.28 2.22zM7.752 6.69l1.092 1.092a2.5 2.5 0 013.374 3.373l1.091 1.092a4 4 0 00-5.557-5.557z"
          ></path>
          <path
            d="M10.748 13.93l2.523 2.523a9.987 9.987 0 01-3.27.547c-4.258 0-7.894-2.66-9.337-6.41a1.651 1.651 0 010-1.186A10.007 10.007 0 012.839 6.02L6.07 9.252a4 4 0 004.678 4.678z"
          ></path></svg
        ><svg
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
          v-if="visible"
          aria-hidden="true"
          class="w-5 h-5"
        >
          <path d="M10 12.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
          <path
            clip-rule="evenodd"
            fill-rule="evenodd"
            d="M.664 10.59a1.651 1.651 0 010-1.186A10.004 10.004 0 0110 3c4.257 0 7.893 2.66 9.336 6.41.147.381.146.804 0 1.186A10.004 10.004 0 0110 17c-4.257 0-7.893-2.66-9.336-6.41zM14 10a4 4 0 11-8 0 4 4 0 018 0z"
          ></path>
        </svg>
        <span class="sr-only">Показать/скрыть пароль</span>
      </button>
    </div>
  </div>
</template>

<script lang="ts" setup>
defineProps({
  idInput: {
    type: String,
    required: true,
  },
  nameInput: {
    type: String,
    required: true,
  },
  typeInput: {
    type: String,
    default: "input",
  },
  visible: {
    type: Boolean,
    default: false,
  },
  modelValue: {
    type: String,
    required: true,
  },
})
const emit = defineEmits({
  update: null,
})
function updateInput(e: any) {
  emit("update:modelValue", e?.target.value)
}
</script>
