<template>
  <hack-modal idModal="registerModal" nameModal="Регистрация">
    <form v-if="!authStore.auth.user" @submit="register" action="#" class="flex flex-col gap-8">
      <hack-input idInput="login" typeInput="login" nameInput="username" v-model.lazy.trim="formData.username.value">
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
      <hack-input idInput="email" typeInput="email" nameInput="email" v-model.trim.lazy="formData.email.value">
        <div class="flex items-center">
          <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
            xmlns="http://www.w3.org/2000/svg">
            <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"></path>
            <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"></path>
          </svg>
          <span class="ml-2">Почта</span>
        </div>
      </hack-input>
      <hack-input idInput="password" typeInput="password" nameInput="password" :visible="formData.visiblePass.value"
        v-model.trim.lazy="formData.password.value" @changeMode="changeMode">
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
        Зарегистроваться
      </hack-button>
    </form>
    <p v-else class="text-default text-3xl text-center">Вы успешно зарегистрированы и авторизированы!</p>
  </hack-modal>
</template>

<script setup lang="ts">
import { ref, Ref } from 'vue'
const authStore = useAuthStore()
const errorElemText = '<p data-error class="mt-2 text-sm text-red-600 dark:text-red-500">{}</p>'
const config = useRuntimeConfig()
interface FormDataType extends Object {
  email: Ref<String>
  username: Ref<String>
  password: Ref<String>
  visiblePass: Ref<Boolean>
}

interface ErrorField extends Object {
  msg: String
  fieldName: String
}

const formData: FormDataType = {
  email: ref(""),
  username: ref(""),
  password: ref(""),
  visiblePass: ref(false),
}

function changeMode(idInput: String) {
  formData.visiblePass.value = !formData.visiblePass.value
  let input = document.querySelector("#" + idInput)
  if (formData.visiblePass.value) input?.setAttribute("type", "text")
  else input?.setAttribute("type", "password")
}

function serialize(data: FormDataType) {
  const errors: ErrorField[] = []
  for (const field in data) {
    if (data.hasOwnProperty(field)) {
      const el = data[field]._value
      if (field === "email") {
        if (/\S+@\S+\.\S+/.test(el) === false) {
          let error: ErrorField = {
            msg: "Напишите действительный email!",
            fieldName: field,
          }
          errors.push(error)
        }
      }
      if (field === "password") {
        if (el.length < 8) {
          let error: ErrorField = {
            msg: "Пароль должен быть не меньше 8 символов!",
            fieldName: field,
          }
          errors.push(error)
        }
      }
      if (field === "username") {
        if (/\W|\N/gm.test(el) === true || el.length === 0) {
          let error: ErrorField = {
            msg: "В логине могут быть только символы латиницы и цифры!",
            fieldName: field,
          }
          errors.push(error)
        }
      }
    }
  }
  return errors
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

async function register(e: any) {
  e.preventDefault()
  removeErrors()
  let errors = serialize(formData)
  if (errors.length) {
    addErrors(errors)
    return 0
  }
  const authToken = await $fetch(`${config.public.apiUrl}/signup/`, {
    method: "POST",
    mode: "cors",
    body: {
      username: formData.username.value,
      email: formData.email.value,
      password: formData.password.value,
    },
    responseType: "json",
    headers: {
      "Content-Type": "application/json; charset=UTF-8",
    },
    async onResponse({ response }) {
      const data = response._data
      const responseCode = response.status
      if (data) {
        if (responseCode != 200) {
          const respErrors: ErrorField[] = []
          for (const field in data) {
            if (data.hasOwnProperty(field)) {
              const el = data[field]
              el.forEach((msg) => {
                let error: ErrorField = {
                  msg: msg,
                  fieldName: field,
                }
                respErrors.push(error)
              })
            }
          }
          addErrors(respErrors)
        }
      }
    },
  })
  if (authToken.hasOwnProperty("token")) {
    await authStore.saveAuthData(authToken.token);
  }
}
</script>
