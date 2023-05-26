<template>
  <hack-modal idModal="loginModal" nameModal="Вход">
    <form v-if="!authStore.auth.user" action="#" @submit="login" class="flex flex-col gap-8">
      <hack-input idInput="loginLog" typeInput="login" nameInput="usernameLogin" v-model.trim.lazy="formData.login.value">
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
      <hack-input idInput="passwordLog" typeInput="password" nameInput="passwordLogin"
        :visible="formData.visiblePass.value" @changeMode="changeMode" v-model.trim.lazy="formData.password.value">
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
    <p v-else class="text-default text-3xl text-center">
      Вы успешно авторизированы!
    </p>
  </hack-modal>
</template>

<script setup lang="ts">
import { ref } from "vue"
const formData = {
  login: ref(""),
  password: ref(""),
  visiblePass: ref(false),
}

const config = useRuntimeConfig()
const errorElemText = '<p data-error class="mt-2 text-sm text-red-600 dark:text-red-500">{}</p>'
const authStore = useAuthStore()
interface ErrorField extends Object {
  msg: String
  fieldName: String
}
function changeMode(idInput: String) {
  formData.visiblePass.value = !formData.visiblePass.value
  let input = document.querySelector("#" + idInput)
  if (formData.visiblePass.value) input?.setAttribute("type", "text")
  else input?.setAttribute("type", "password")
}

function removeErrors() {
  document.querySelectorAll("[data-error]").forEach((el) => el.remove())
  document.querySelectorAll("label").forEach((el) => {
    el.classList.remove("!text-red-600")
    el.classList.remove("!dark:text-red-500")
  })
  document.querySelectorAll("svg").forEach((el) => {
    el.classList.remove("!text-red-600")
    el.classList.remove("!dark:text-red-500")
  })
}

function addErrors(errors: ErrorField[]) {
  for (const error in errors) {
    if (errors.hasOwnProperty(error)) {
      const el = errors[error]
      const fieldElParent = document.querySelector(`[name=${el.fieldName}]`)?.parentElement
      fieldElParent?.querySelector("label")?.classList.add("!text-red-600")
      fieldElParent?.querySelector("label")?.classList.add("!dark:text-red-500")
      fieldElParent?.querySelector("svg")?.classList.add("!text-red-600")
      fieldElParent?.querySelector("svg")?.classList.add("!dark:text-red-500")
      fieldElParent?.insertAdjacentHTML("afterend", errorElemText.replace("{}", el.msg))
    }
  }
}
async function login(e: any) {
  e.preventDefault()
  removeErrors()
  const authToken: Object = await $fetch(`${config.public.apiUrl}/login/`, {
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
      const data = response._data
      const responseCode = response.status
      if (data) {
        if (responseCode != 200) {
          console.log(data)
          const respErrors: ErrorField[] = []
          const el = data.detail
          console.log(el)
          let error: ErrorField = {
            msg: el,
            fieldName: /password/.test(el) ? "passwordLogin" : "usernameLogin",
          }
          console.log(error)
          respErrors.push(error)
          addErrors(respErrors)
        }
      }
    },
    async onRequestError({ request, error }) {
      // Log error
      console.log("[fetch request error]", request, error)
    },
  })
  if (authToken.hasOwnProperty("token")) {
    await authStore.saveAuthData(authToken.token)
  }
}
</script>
