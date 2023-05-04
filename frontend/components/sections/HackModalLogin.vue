<template>
  <hack-modal idModal="loginModal" nameModal="Вход">
    <form action="#" @submit="login" class="flex flex-col gap-8">
      <hack-input idInput="loginLog" typeInput="login" nameInput="loginLog" v-model.trim.lazy="formData.login.value">
        <div class="flex items-center">
          <svg fill="currentColor" class="w-5 h-5" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true">
            <path clip-rule="evenodd" fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.536-4.464a.75.75 0 10-1.061-1.061 3.5 3.5 0 01-4.95 0 .75.75 0 00-1.06 1.06 5 5 0 007.07 0zM9 8.5c0 .828-.448 1.5-1 1.5s-1-.672-1-1.5S7.448 7 8 7s1 .672 1 1.5zm3 1.5c.552 0 1-.672 1-1.5S12.552 7 12 7s-1 .672-1 1.5.448 1.5 1 1.5z">
            </path>
          </svg>
          <span class="ml-2">Логин</span>
        </div>
      </hack-input>
      <hack-input idInput="passwordLog" typeInput="password" nameInput="passwordLog" :visible="formData.visiblePass.value"
        @changeMode="changeMode" v-model.trim.lazy="formData.password.value">
        <div class="flex items-center">
          <svg fill="currentColor" viewBox="0 0 20 20" class="w-5 h-5" xmlns="http://www.w3.org/2000/svg"
            aria-hidden="true">
            <path clip-rule="evenodd" fill-rule="evenodd"
              d="M10 1a4.5 4.5 0 00-4.5 4.5V9H5a2 2 0 00-2 2v6a2 2 0 002 2h10a2 2 0 002-2v-6a2 2 0 00-2-2h-.5V5.5A4.5 4.5 0 0010 1zm3 8V5.5a3 3 0 10-6 0V9h6z">
            </path>
          </svg>
          <span class="ml-2">Пароль</span>
        </div>
      </hack-input>
      <hack-button type="submit" typeBtn="solid"
        class="!bg-accent-400 !border-accent-400 hover:!bg-accent-500 hover:!border-accent-500 !text-default">
        Войти
      </hack-button>
    </form>
  </hack-modal>
</template>

<script setup lang="ts">
const formData = {
  login: ref(""),
  password: ref(""),
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
