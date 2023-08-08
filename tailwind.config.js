const defaultTheme = require("tailwindcss/defaultTheme");

module.exports = {
  content: ["./public/*.html"],
  theme: {
    screens: {
      ...defaultTheme.screens,
      sm: "51px",
    },
  },
  plugins: [],
};
