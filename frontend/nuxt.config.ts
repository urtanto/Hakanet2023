// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  extends: ["nuxt-seo-kit"],
  vite: {
    server: {
      hmr: {
        protocol: "ws",
        host: "0.0.0.0",
      },
    },
  }, 
  components: [
    {
      path: '~/components', // will get any components nested in let's say /components/test too
      pathPrefix: false,
    },
  ],
  modules: ["@nuxtjs/tailwindcss", "nuxt-purgecss", "nuxt-svgo", "@nuxt/image-edge"],
  runtimeConfig: {
    trailingSlash: true,
    indexable: false,
    public: {
      siteUrl: "http:/localhost:3000",
      siteName: "Hackaton Site",
      siteDescription: "Site base on Nuxt.",
      language: "ru-RU",
      titleSeparator: "|",
      trailingSlash: false,
    },
  },
  postcss: {
    preset: {
      autoprefixer: {
        grid: true,
        flexbox: true,
      },
    },
  },
})
