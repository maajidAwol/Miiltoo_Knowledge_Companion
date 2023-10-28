const hamb_btn = document.getElementById("hamb-menu");
const line = document.querySelector(".line");
const nav_drop = document.querySelector(".home-group");
const btn_drop = document.querySelector(".dropdown");
const drop_content = document.querySelector(".dropdown-content");
const icon_drop = document.querySelector(".drop-icon");
hamb_btn.addEventListener("click", function () {
  nav_drop.classList.toggle("slide");
  hamb_btn.classList.toggle("active");
});
btn_drop.addEventListener("click", () => {
  icon_drop.classList.toggle("up");
  drop_content.classList.toggle("visibility");
  icon_drop.classList.toggle("i-rotate");
});
window.addEventListener("load", function () {
  window.scrollTo(0, 0);
});
