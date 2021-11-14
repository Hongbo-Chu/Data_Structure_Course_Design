module.exports = {
  purge: [],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {maxHeight: ['focus'],
    backgroundColor: ['active'],
    backgroundColor: ['group-focus'],
    translate: ['motion-reduce'],
    },
  },
  plugins: [],
}
