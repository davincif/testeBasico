var app = new Vue({
  el: "#vue-app",
  delimiters: ["[[", "]]"],
  data: {
    editing: false,
    everClicked: false,
  },
  methods: {
    editToggle: function (event) {
      event.preventDefault();

      this.editing = !this.editing;
      this.everClicked = true;
    },
    deleteClassroom: function (event) {
      event.preventDefault();

      $("#save-form-btn").click();
    },
  },
});
