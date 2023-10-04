const hamb_btn = document.getElementById("hamb-menu");
const line = document.querySelector(".line");
const nav_links = document.querySelector(".nav-links");
const drop_content = document.querySelector(".dropdown-content");
const overlay = document.querySelector(".overlay");
const body = document.querySelector(".body");
hamb_btn.addEventListener("click", function () {
nav_links.classList.toggle("slide");
hamb_btn.classList.toggle("active");
overlay.classList.toggle("hidden");
body.classList.toggle("overflow-hidden");

});
overlay.addEventListener("click", () => {
nav_links.classList.toggle("slide");
hamb_btn.classList.toggle("active");
overlay.classList.toggle("hidden");
body.classList.toggle("overflow-hidden");

});
window.addEventListener("load", function () {
window.scrollTo(0, 0);
});
