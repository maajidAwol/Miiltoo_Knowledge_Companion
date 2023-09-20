const hamb_btn = document.getElementById("hamb-menu");
const nav_drop = document.querySelector(".nav-dropdown");
const overlay = document.getElementById("overlay-nav");
const close_hamb = document.querySelector(".close-menu");
const body = document.querySelector(".bod");
hamb_btn.addEventListener("click", function () {
  hamb_btn.style.display = "none";
  console.log("hamb");
  overlay.classList.remove("hidden");
  nav_drop.classList.remove("hidden");
  close_hamb.classList.remove("hidden");
  body.classList.add("overflow-hid");
});
close_hamb.addEventListener("click", function () {
  close_hamb.classList.add("hidden");
  hamb_btn.style.display = "block";
  nav_drop.classList.add("hidden");
  overlay.classList.add("hidden");
  body.classList.remove("overflow-hid");
});
overlay.addEventListener("click", function () {
  close_hamb.classList.add("hidden");
  hamb_btn.style.display = "block";
  nav_drop.classList.add("hidden");
  overlay.classList.add("hidden");
  body.classList.remove("overflow-hid");
});
