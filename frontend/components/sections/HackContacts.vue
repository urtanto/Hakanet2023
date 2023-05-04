<template>
  <section>
    <div
      class="h-[40rem] bg-blend-multiply bg-no-repeat bg-center bg-cover bg-fixed bg-accent/[.75] bg-[url(~/assets/images/banners/contact.jpg)]"
    >
      <div class="px-6 pt-28 pb-5 mx-auto flex flex-col items-center gap-4">
        <h2 class="text-default tracking-tight font-bold text-4xl m-0">Остались вопросы?</h2>
        <p class="text-default text-lg mb-16">Мы будем рады ответить на всё, что осталось под вопросом!</p>
      </div>
    </div>
    <div class="py-6 pb-24 mt-[-24rem] my-auto">
      <form
        action="#"
        method="GET"
        class="bg-accent-700 max-w-3xl mx-auto mb-28 gap-8 grid grid-cols-2 shadow-sm p-6 rounded-lg"
      >
        <hack-input
          idInput="firstNameContact"
          typeInput="text"
          nameInput="firstNameContact"
          v-model.lazy.trim="formData.firstName.value"
        >
          <div class="flex items-center">
            <svg
              fill="currentColor"
              class="w-5 h-5"
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
            <span class="ml-2">Имя</span>
          </div>
        </hack-input>
        <hack-input
          idInput="lastNameContact"
          typeInput="text"
          nameInput="lastNameContact"
          v-model.lazy.trim="formData.lastName.value"
        >
          <div class="flex items-center">
            <svg
              fill="currentColor"
              class="w-5 h-5"
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
            <span class="ml-2">Фамилия</span>
          </div>
        </hack-input>
        <hack-input
          idInput="emailContact"
          typeInput="email"
          nameInput="emailContact"
          v-model.lazy.trim="formData.email.value"
        >
          <div class="flex items-center">
            <svg
              aria-hidden="true"
              class="w-5 h-5"
              fill="currentColor"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"></path>
              <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"></path>
            </svg>
            <span class="ml-2">Почта</span>
          </div>
        </hack-input>
        <hack-input
          idInput="phoneContact"
          typeInput="phone"
          nameInput="phoneContact"
          v-model.lazy.trim="formData.phone.value"
        >
          <div class="flex items-center">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-5 h-5"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M10.5 1.5H8.25A2.25 2.25 0 006 3.75v16.5a2.25 2.25 0 002.25 2.25h7.5A2.25 2.25 0 0018 20.25V3.75a2.25 2.25 0 00-2.25-2.25H13.5m-3 0V3h3V1.5m-3 0h3m-3 18.75h3"
              />
            </svg>
            <span class="ml-2">Телефон</span>
          </div>
        </hack-input>
        <div class="col-span-2">
          <label
            for="message"
            class="block mb-2 text-sm font-medium text-default"
            >Собщение</label
          >
          <textarea
            id="message"
            rows="4"
            class="block p-2.5 resize-y w-full text-sm text-default focus:ring-accent focus:border-accent bg-accent-900 rounded-lg placeholder-default-dark"
            placeholder="Напишите свои вопросы здесь..."
          ></textarea>
        </div>
        <hack-button
          typeBtn="solid"
          class="!bg-accent-400 !border-accent-400 hover:!bg-accent-500 hover:!border-accent-500 !text-default"
          >Отправить</hack-button
        >
      </form>
      <ul class="grid grid-cols-3 gap-3">
        <li class="px-5">
          <div>
            <div
              class="w-16 h-16 bg-accent-600 text-default rounded-lg flex items-center justify-center mb-4 mx-auto"
            >
              <svg
                class="w-8 h-8"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"></path>
                <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"></path>
              </svg>
            </div>
            <h3 class="font-bold text-black text-lg mb-2 m-0 text-center">Наша почта</h3>
            <p class="text-center text-gray-700 mb-2">
            Пишите нам по электронной почте для общих вопросов, включая&nbsp;маркетинговые и партнерские возможности.
            </p>
            <a
               href="mailto:shoeway@stylelifeweb.su"
              class="text-center inline-block w-full text-accent-600 font-bold underline hover:no-underline"
              aria-current="location"
              >
              shoeway@stylelifeweb.su
            </a>
          </div>
        </li>
        <li class="px-5">
          <div>
            <div
              class="w-16 h-16 bg-accent-600 text-default rounded-lg flex items-center justify-center mb-4 mx-auto"
            >
              <svg
                class="w-8 h-8"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z"></path>
                <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z"></path>
              </svg>
            </div>
            <h3 class="font-bold text-black text-lg mb-2 m-0 text-center">Поситите нас</h3>
            <p class="text-center text-gray-700 mb-2">
            Мы работаем с <span class="text-accent-800 text-bold">Понедльника по Пятницу</span> с <span class="text-accent-800 text-bold">08:00 до 18:00</span></p>
<a href="https://yandex.ru/maps/-/CCUgVStisD" class="text-center inline-block w-full text-accent-600 font-bold underline hover:no-underline">г. Тюмень, улица 25 Октября, 23Ас1</a>

          </div>
        </li>
        <li class="px-5">
          <div>
            <div
              class="w-16 h-16 bg-accent-600 text-default rounded-lg flex items-center justify-center mb-4 mx-auto"
            >
              <svg
                class="w-8 h-8"
                fill="currentColor"
                viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg"
              >
<path d="M2 3a1 1 0 011-1h2.153a1 1 0 01.986.836l.74 4.435a1 1 0 01-.54 1.06l-1.548.773a11.037 11.037 0 006.105 6.105l.774-1.548a1 1 0 011.059-.54l4.435.74a1 1 0 01.836.986V17a1 1 0 01-1 1h-2C7.82 18 2 12.18 2 5V3z"></path>
              </svg>
            </div>
            <h3 class="font-bold text-black text-lg mb-2 m-0 text-center">Позвоните нам</h3>
            <p class="text-center text-gray-700 mb-2">
            Позвоните нам, чтобы поговорить с одним из членов нашей команды. Мы всегда рады помочь.
            </p>
            <a
               href="tel:88005553535"
              class="text-center inline-block w-full text-accent-600 font-bold underline hover:no-underline"
              >
              +7 (800) 555-35-35
            </a>
          </div>
        </li>
      </ul>
    </div>
  </section>
</template>

<style scoped></style>

<script setup lang="ts">
import { ref } from "vue"
import HackLink from "~/components/UI/HackLink"

const formData = {
  firstName: ref(""),
  lastName: ref(""),
  email: ref(""),
  phone: ref(""),
  mesage: ref(""),
}
</script>
