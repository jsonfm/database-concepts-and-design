/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./app/templates/**/*.html",
  "./app/static/s/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
}

