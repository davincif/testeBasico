var app = new Vue({
  el: "#vue-app",
  delimiters: ["[[", "]]"],
  data: {
    editing: false,
  },
  methods: {
    editToggle: function (event) {
      this.editing = !this.editing;
      event.preventDefault();
    },
  },
});
