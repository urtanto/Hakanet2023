import { defineStore } from "pinia"
import { useRuntimeConfig } from "nuxt/app"

interface User extends Object {
  last_login: string | null
  is_superuser: boolean
  username: string
  first_name: string
  last_name: string
  email: string
  is_active: boolean
  date_joined: string
}

interface Auth extends Object {
  token: string,
  user: User
}

export const useAuthStore = defineStore("authStore", {
  state: () => ({
    auth: {},
  }),
  getters: {
    getUserInfo(): User {
      return this.auth?.user
    },
    getToken(): string {
      return this.auth?.token
    },
    getUserFN(): string {
      return this.getUserInfo.first_name + ' ' + this.getUserInfo.last_name
    }
  },
  actions: {
    async saveAuthData(token: string) {
      this.auth = {token: token, user: {} as User} as Auth;
      const config = useRuntimeConfig()
      const data = await $fetch(`${config.public.apiUrl}/get/user/`, {
      method: "GET",
      mode: "cors",
      parseResponse: JSON.parse,
      responseType: "json",
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
        Authorization: `Token ${this.getToken}`,
      },
    })
    this.auth["user"] = data.user
    },
    async deleteAuthData() {
      const config = useRuntimeConfig()
      await $fetch(`${config.public.apiUrl}/logout`,  {
      method: "POST",
      mode: "cors",
      parseResponse: JSON.parse,
      responseType: "json",
      headers: {
        "Content-Type": "application/json; charset=UTF-8",
        Authorization: `Token ${this.getToken}`,
      },
      })
      this.auth = {}
    }
  }
})
