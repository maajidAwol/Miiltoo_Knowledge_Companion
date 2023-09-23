const forget = document.querySelector(".link-forget");
const text_btn_signup = document.querySelector(".text-btn-signup");
const eye_icon = document.querySelector(".icon-pass i");
const password_field = document.getElementById("password-field");
const btn_login = document.querySelector(".btn-login");
eye_icon.addEventListener("click", () => {
  if (password_field.type == "password") {
    password_field.type = "text";
    eye_icon.classList.replace("fa-eye-slash", "fa-eye");
  } else {
    password_field.type = "password";
    eye_icon.classList.replace("fa-eye", "fa-eye-slash");
  }
});
forget.addEventListener("click", (event) => {
  event.preventDefault();
  window.location.href = "http://127.0.0.1:5500/templates/login.html#forget";
});
text_btn_signup.addEventListener("click", (event) => {
  event.preventDefault();
  window.location.href = "http://127.0.0.1:5500/templates/signup.html";
});
