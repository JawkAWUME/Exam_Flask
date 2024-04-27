/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: [
   
    "./node_modules/flowbite/**/*.js",'./src/**/*.html',
    './src/**/*.css',
    './src/**/*.jsx'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require("flowbite/plugin"),
    require('tailwindcss'),
    require('autoprefixer'),
],
}

