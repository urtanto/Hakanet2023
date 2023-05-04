<template>
  <hack-modal
    idModal="loginModal"
    nameModal="Вход"
  >
    <form
      action="#"
      @submit="login"
      class="flex flex-col gap-8"
    >
      <hack-input
        idInput="loginLog"
        typeInput="login"
        nameInput="loginLog"
        v-model.trim.lazy="formData.login.value"
      >
        <div class="flex items-center">
          <svg
            fill="currentColor"
            class="w-5 h-5 text-gray-500 dark:text-gray-400"
            viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
          >
            <path
              clip-rule="evenodd"
              fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.536-4.464a.75.75 0 10-1.061-1.061 3.5 3.5 0 01-4.95 0 .75.75 0 00-1.06 1.06 5 5 0 007.07 0zM9 8.5c0 .828-.448 1.5-1 1.5s-1-.672-1-1.5S7.448 7 8 7s1 .672 1 1.5zm3 1.5c.552 0 1-.672 1-1.5S12.552 7 12 7s-1 .672-1 1.5.448 1.5 1 1.5z"
            ></path>
          </svg>
          <span class="ml-2">Логин</span>
        </div>
      </hack-input>
      <hack-input
        idInput="passwordLog"
        typeInput="password"
        nameInput="passwordLog"
        :visible="formData.visiblePass.value"
        @changeMode="changeMode"
        v-model.trim.lazy="formData.password.value"
      >
        <div class="flex items-center">
          <svg
            fill="currentColor"
            viewBox="0 0 20 20"
            class="w-5 h-5 text-gray-500 dark:text-gray-400"
            xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true"
          >
            <path
              clip-rule="evenodd"
              fill-rule="evenodd"
              d="M10 1a4.5 4.5 0 00-4.5 4.5V9H5a2 2 0 00-2 2v6a2 2 0 002 2h10a2 2 0 002-2v-6a2 2 0 00-2-2h-.5V5.5A4.5 4.5 0 0010 1zm3 8V5.5a3 3 0 10-6 0V9h6z"
            ></path>
          </svg>
          <span class="ml-2">Пароль</span>
        </div>
      </hack-input>
      <div class="flex items-center">
        <input
          checked
          id="checkboxlog"
          name="checkboxlog"
          type="checkbox"
          :value="formData.accepted"
          class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
        />
        <label
          for="checkboxlog"
          name="checkboxlog"
          class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300"
          >Я согласен с
          <nuxt-link
            to="#"
            class="text-blue-600 hover:underline dark:text-blue-500"
            >правилами пользования Сайта</nuxt-link
          >.</label
        >
      </div>
      <button
        type="submit"
        class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800"
      >
        Войти
      </button>
    </form>
  </hack-modal>
</template>

<script setup lang="ts">
const formData = {
  login: ref(""),
  password: ref(""),
  accepted: ref(false),
  visiblePass: ref(false),
}

function changeMode(idInput: String) {
  formData.visiblePass.value = !formData.visiblePass.value
  let input = document.querySelector("#" + idInput)
  if (formData.visiblePass.value) input?.setAttribute("type", "text")
  else input?.setAttribute("type", "password")
}

async function login(e: any) {
  e.preventDefault()
  const authToken: Object = await $fetch("http://localhost:8000/login/", {
    method: "POST",
    mode: "cors",
    body: {
      username: formData.login.value,
      password: formData.password.value,
    },
    parseResponse: JSON.parse,
    responseType: "json",
    headers: {
      "Content-Type": "application/json; charset=UTF-8",
    },
    async onResponse({ response }) {
      return response._data
    },
    async onRequestError({ request, error }) {
      // Log error
      console.log("[fetch request error]", request, error)
    },
  })
  console.log(authToken)
  if (authToken.hasOwnProperty("token")) {
    return await $fetch("http://localhost:8000/test/", {
      method: "GET",
      mode: "cors",
      parseResponse: JSON.parse,
      responseType: "json",
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
        Authorization: `Token ${authToken.token}`,
      },
      async onResponse({ request, options, response }) {
        console.log(request, response)
      },
      async onRequestError({ request, options, error }) {
        // Log error
        console.log("[fetch request error]", request, error)
      },
    })
  }
}
</script>
