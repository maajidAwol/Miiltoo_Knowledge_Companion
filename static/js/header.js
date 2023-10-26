const home_link = document.querySelectorAll(".home-link");
const underline = document.getElementById("underline");
const grade_menu = document.querySelector(".grade-menu");
const grade_btn_icon = document.querySelector(".grade-btn-icon");
const profile_drop_icon = document.querySelector(".profile-drop-icon");
const profile_group = document.querySelector(".profile-group");
const profile_menu = document.querySelector(".profile-menu");
const body = document.querySelector(".body");
let currentPosition;
let n = 0;
body.addEventListener("click", () => {
  grade_menu.classList.add("hidden");
  profile_menu.classList.add("hidden");
  grade_btn_icon.style.transform = "rotate(0deg)";
  profile_drop_icon.style.transform = "rotate(0deg)";
});
const mediaQuery_768 = window.matchMedia("(min-width: 768px)");
if (mediaQuery_768.matches) {
  for (let i = 0; i < home_link.length; i++) {
    home_link[i].addEventListener("mouseover", () => {
      if (i === 0) {
        n = 73 * i;
        currentPosition = 0;
        grade_menu.classList.add("hidden");
        profile_menu.classList.add("hidden");
        grade_btn_icon.style.transform = "rotate(0deg)";
        profile_drop_icon.style.transform = "rotate(0deg)";
      } else if (i === 1) {
        n = 73 * i;
        grade_menu.classList.remove("hidden");
        profile_menu.classList.add("hidden");
        grade_btn_icon.style.transform = "rotate(180deg)";
        profile_drop_icon.style.transform = "rotate(0deg)";
        currentPosition = 1;
      } else if (i === 2) {
        n = 90 * i;
        currentPosition = 0;
        grade_menu.classList.add("hidden");
        profile_menu.classList.add("hidden");
        grade_btn_icon.style.transform = "rotate(0deg)";
        profile_drop_icon.style.transform = "rotate(0deg)";
      } else {
        n = 94 * i;
        currentPosition = 0;
        grade_menu.classList.add("hidden");
        profile_menu.classList.add("hidden");
        grade_btn_icon.style.transform = "rotate(0deg)";
        profile_drop_icon.style.transform = "rotate(0deg)";
      }
      underline.style.transform = `translateX(${n}px)`;
    });
    home_link[i].addEventListener("mouseleave", function () {
      underline.style.transform = `translateX(${currentPosition})`;
    });
  }
} else {
  underline.style.display = "none";
}
profile_group.addEventListener("mouseover", () => {
  profile_menu.classList.remove("hidden");
  grade_menu.classList.add("hidden");
  grade_btn_icon.style.transform = "rotate(0deg)";
  profile_drop_icon.style.transform = "rotate(180deg)";
});
const upload_btn = document.querySelector("#upload-btn1");
const upload_popup = document.querySelector(".upload-popup");
const close_btn = document.querySelector(".close-popup");
const overlay = document.querySelectorAll(".overlay");

upload_btn.addEventListener("click", (e) => {
  e.preventDefault();
  upload_popup.classList.toggle("hidden");
  overlay[1].classList.toggle("hidden");
  document.querySelector(".body").style.overflowY = "hidden";
});
close_btn.addEventListener("click", () => {
  upload_popup.classList.toggle("hidden");
  overlay[1].classList.toggle("hidden");
  document.querySelector(".body").style.overflowY = "auto";
});
overlay[1].addEventListener("click", () => {
  upload_popup.classList.toggle("hidden");
  overlay[1].classList.toggle("hidden");
  document.querySelector(".body").style.overflowY = "auto";
});
const hamb_btn = document.getElementById("hamb-menu");
const line = document.querySelector(".line");
const nav_links = document.querySelector(".nav-links");
const drop_content = document.querySelector(".dropdown-content");
hamb_btn.addEventListener("click", function () {
  nav_links.classList.toggle("slide");
  hamb_btn.classList.toggle("active");
  overlay[0].classList.toggle("hidden");
  body.classList.toggle("overflow-hidden");
});
overlay[0].addEventListener("click", () => {
  nav_links.classList.toggle("slide");
  hamb_btn.classList.toggle("active");
  overlay.classList.toggle("hidden");
  body.classList.toggle("overflow-hidden");
});
window.addEventListener("load", function () {
  window.scrollTo(0, 0);
});
