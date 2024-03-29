import path from "path"

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
      path: "~/components", // will get any components nested in let's say /components/test too
      pathPrefix: false,
    },
  ],
  modules: ["@nuxtjs/tailwindcss", "nuxt-svgo", "@nuxt/image-edge", "@nuxt/image-edge", "@pinia/nuxt"],
  runtimeConfig: {
    trailingSlash: true,
    indexable: false,
    public: {
      apiUrl: "http://127.0.0.1:8000",
      siteUrl: "http:/127.0.0.1:3000",
      siteName: "Hackaton Site",
      siteDescription: "Site base on Nuxt.",
      language: "ru-RU",
      titleSeparator: "|",
      trailingSlash: false,
    },
  },
  imports: {
    dirs: ["./store"],
  },
  postcss: {
    preset: {
      autoprefixer: {
        grid: true,
        flexbox: true,
      },
      tailwindcss: path.resolve(__dirname, "./tailwind.config.ts"),
    },
  },
})
