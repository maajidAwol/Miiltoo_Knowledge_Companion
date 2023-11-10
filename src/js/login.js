const forget = document.querySelector(".link-forget");
const eye_icon1 = document.querySelector(".icon-pass i");
const text_btn_signup = document.querySelector(".text-btn-signup");
// const text_btn_login = document.querySelector(".text-btn-login");
const eye_icon2 = document.querySelector(".icon-confirm i");
const password_field = document.getElementById("password-field");
const confirm_field = document.getElementById("confirm-field");
const btn_login = document.querySelector(".btn-login");
const btn_close = document.querySelector(".btn-close");
eye_icon1.addEventListener("click", () => {
  if (password_field.type == "password") {
    password_field.type = "text";
    eye_icon1.classList.replace("fa-eye-slash", "fa-eye");
  } else {
    password_field.type = "password";
    eye_icon1.classList.replace("fa-eye", "fa-eye-slash");
  }
});
eye_icon2.addEventListener("click", () => {
  if (confirm_field.type == "password") {
    confirm_field.type = "text";
    eye_icon2.classList.replace("fa-eye-slash", "fa-eye");
  } else {
    confirm_field.type = "password";
    eye_icon2.classList.replace("fa-eye", "fa-eye-slash");
  }
});
forget.addEventListener("click", (event) => {
  event.preventDefault();
  window.location.href = "/forget";
});
text_btn_signup.addEventListener("click", (event) => {
  event.preventDefault();
  window.location.href = "/signup";
});
// text_btn_login.addEventListener("click", (event) => {
//   console.log("clicked");
//   event.preventDefault();
//   window.location.href = "/login";
// });
btn_close.addEventListener("click", (event) => {
  event.preventDefault();
  window.location.href = "/";
});
