import type { Config } from "tailwindcss"

export default <Partial<Config>>{
  plugins: [require("flowbite")],
  content: ["./node_modules/flowbite.{js,ts}"],
  theme: {
    colors: {
      accent: "216146",
      default: "eae9e7",
    },
  },
}
