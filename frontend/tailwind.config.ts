import type { Config } from "tailwindcss"

export default <Partial<Config>>{
  plugins: [require("flowbite")],
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./nuxt.config.{js,ts}",
    "./node_modules/flowbite/**/*.{js,ts}",
  ],
  theme: {
    extend: {
      colors: {
        accent: {
          DEFAULT: "#216146",
          900: "#267051",
          800: "#2b7e5b",
          700: "#308d66",
          600: "#359c70",
          500: "#3aaa7b",
          400: "#3fb985",
        },
        default: {
          DEFAULT: "#EAE9E7",
          dark: "#CCCACA",
        },
      },
      fontFamily: {
        base: ["Bahnschrift", "sans-serif"],
      },
      screens: {
        sm: "460px",
      },
    },
  },
}
