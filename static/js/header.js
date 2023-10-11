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
for (let i = 0; i < home_link.length; i++) {
  home_link[i].addEventListener("mouseover", () => {
    if (i === 0) {
      n = 78 * i;
      currentPosition = 0;
      grade_menu.classList.add("hidden");
      profile_menu.classList.add("hidden");
      grade_btn_icon.style.transform = "rotate(0deg)";
      profile_drop_icon.style.transform = "rotate(0deg)";
    } else if (i === 1) {
      n = 78 * i;
      grade_menu.classList.remove("hidden");
      profile_menu.classList.add("hidden");
      grade_btn_icon.style.transform = "rotate(180deg)";
      profile_drop_icon.style.transform = "rotate(0deg)";

      currentPosition = 1;
    } else if (i === 2) {
      n = 95 * i;
      currentPosition = 0;
      grade_menu.classList.add("hidden");
      profile_menu.classList.add("hidden");
      grade_btn_icon.style.transform = "rotate(0deg)";
      profile_drop_icon.style.transform = "rotate(0deg)";
    } else {
      n = 99 * i;
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
profile_group.addEventListener("mouseover", () => {
  profile_menu.classList.remove("hidden");
  grade_menu.classList.add("hidden");
  grade_btn_icon.style.transform = "rotate(0deg)";
  profile_drop_icon.style.transform = "rotate(180deg)";
});
