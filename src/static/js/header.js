const home_link = document.querySelectorAll(".home-link");
const underline = document.getElementById("underline");
const grade_menu = document.querySelector(".grade-menu");
const country_menu = document.querySelector(".country-menu");
const page_menu = document.querySelector(".page-menu");
const grade_btn_icon = document.querySelectorAll(".grade-btn-icon");
const profile_drop_icon = document.querySelector(".profile-drop-icon");
const profile_group = document.querySelector(".profile-group");
const profile_menu = document.querySelector(".profile-menu");
const upload_btn = document.querySelector("#upload-btn1");
const upload_popup = document.querySelector(".upload-popup");
const close_btn = document.querySelector(".close-popup");
const overlay = document.querySelector(".overlay");
const hamb_btn = document.getElementById("hamb-menu");
const line = document.querySelector(".line");
const nav_links = document.querySelector(".nav-links");
const nav_links_A5 = document.querySelector(".upload-links");
const drop_content = document.querySelector(".dropdown-content");

const body = document.querySelector(".body");
let currentPosition;
let n = 0;

const mediaQuery_992 = window.matchMedia("(width==992px)");
const mediaQuery_768 = window.matchMedia("(width==768px)");
const mediaQuery_600 = window.matchMedia("(width==600px)");
const mediaQuery_360 = window.matchMedia("(width== 360px)");
if (
  mediaQuery_360.matches ||
  mediaQuery_600.matches ||
  mediaQuery_768.matches ||
  mediaQuery_992.matches
) {
  location.reload();
}

body.addEventListener("click", () => {
  grade_menu.classList.add("hidden");
  country_menu.classList.add("hidden");
  page_menu.classList.add("hidden");
  profile_menu.classList.add("hidden");
  grade_btn_icon.forEach((grade_btn_icon) => {
    grade_btn_icon.style.transform = "rotate(0deg)";
  });
  profile_drop_icon.style.transform = "rotate(0deg)";
});
if (window.matchMedia("(min-width:992px)").matches) {
  nav_links_A5.classList.replace("home-link", "upload-links");
} else {
  nav_links_A5.classList.replace("upload-links", "home-link");
}
for (let i = 0; i < home_link.length; i++) {
  home_link[i].addEventListener("mouseover", () => {
    if (i === 0) {
      n = 43 * i;
      currentPosition = 0;
      if (window.matchMedia("(min-width:992px)").matches) {
        grade_menu.classList.add("hidden");
        profile_menu.classList.add("hidden");
        page_menu.classList.add("hidden");
        country_menu.classList.add("hidden");
        grade_btn_icon[i].style.transform = "rotate(0deg)";
        profile_drop_icon.style.transform = "rotate(0deg)";
      }
    } else if (i === 1) {
      n = 73 * i;
      grade_menu.classList.remove("hidden");

      if (window.matchMedia("(min-width:992px)").matches) {
        profile_menu.classList.add("hidden");
        page_menu.classList.add("hidden");
        country_menu.classList.add("hidden");
        grade_btn_icon[i].style.transform = "rotate(180deg)";
        profile_drop_icon.style.transform = "rotate(0deg)";
        currentPosition = i;
      }
    } else if (i === 2) {
      n = 90 * i;
      if (window.matchMedia("(min-width:992px)").matches) {
        currentPosition = i;
        grade_menu.classList.add("hidden");
        profile_menu.classList.add("hidden");
        page_menu.classList.add("hidden");
        country_menu.classList.add("hidden");
        grade_btn_icon[i].style.transform = "rotate(0deg)";
        profile_drop_icon.style.transform = "rotate(0deg)";
      }
    } else if (i === 3) {
      n = 94 * i;
      page_menu.classList.remove("hidden");

      if (window.matchMedia("(min-width:992px)").matches) {
        currentPosition = i;
        country_menu.classList.add("hidden");
        profile_menu.classList.add("hidden");
        grade_menu.classList.add("hidden");
        grade_btn_icon[i - 2].style.transform = "rotate(180deg)";
        profile_drop_icon.style.transform = "rotate(0deg)";
      }
    } else {
      n = 0;
      country_menu.classList.remove("hidden");

      if (window.matchMedia("(min-width:992px)").matches) {
        currentPosition = i;
        page_menu.classList.add("hidden");
        grade_menu.classList.add("hidden");
        profile_menu.classList.add("hidden");
        grade_btn_icon[i - 2].style.transform = "rotate(180deg)";
        profile_drop_icon.style.transform = "rotate(0deg)";
      }
    }
    underline.style.transform = `translateX(${n}px)`;
  });
  home_link[i].addEventListener("mouseleave", function () {
    underline.style.transform = `translateX(${currentPosition})`;
  });
  home_link[i].addEventListener("click", function (event) {
    if (window.matchMedia("(max-width:992px)").matches) {
      if (i != 1 || i != 3) {
        event.preventDefault();
      }
    }
    underline.style.transform = `translateX(${i})`;
  });
}
hamb_btn.addEventListener("click", function () {
  nav_links.classList.toggle("slide");
  hamb_btn.classList.toggle("active");
  overlay.classList.toggle("hidden");
  upload_popup.classList.add("hidden");
  overlay.style.zIndex = "1";

  // body.classList.toggle("overflow-hidden");
});
overlay.addEventListener("click", () => {
  nav_links.classList.toggle("slide");
  hamb_btn.classList.toggle("active");
  overlay.classList.toggle("hidden");
  overlay.classList.toggle("forMob");
  // body.classList.toggle("overflow-hidden");
});
profile_group.addEventListener("mouseover", () => {
  profile_menu.classList.remove("hidden");
  grade_menu.classList.add("hidden");
  page_menu.classList.add("hidden");
  country_menu.classList.add("hidden");
  grade_btn_icon.style.transform = "rotate(0deg)";
  profile_drop_icon.style.transform = "rotate(180deg)";
});
uploadFunc();
function uploadFunc() {
  upload_btn.addEventListener("click", (e) => {
    e.preventDefault();
    upload_popup.classList.toggle("hidden");
    overlay.style.display = "block";
    document.querySelector(".body").style.overflowY = "hidden";
    overlay.classList.remove("forMob");
    overlay.style.zIndex = "3";
  });
}
close_btn.addEventListener("click", () => {
  overlay.style.display = "none";
  upload_popup.classList.toggle("hidden");
  document.querySelector(".body").style.overflowY = "auto";
  overlay.classList.remove("forMob");
});
overlay.addEventListener("click", () => {
  overlay.classList.toggle("hidden");
  upload_popup.classList.toggle("hidden");
  document.querySelector(".body").style.overflowY = "auto";
  overlay.classList.remove("forMob");
});

// var mediaQuery = window.matchMedia("(min-width: 768px)");
// if (mediaQuery.matches) {
//   hamb_btn.classList.toggle("hidden");
// }

window.addEventListener("load", function () {
  window.scrollTo(0, 0);
});
// Add event listeners to anchor links
document.addEventListener("DOMContentLoaded", function () {
  var links = document.querySelectorAll('a[href^="#"]');
  for (var i = 0; i < links.length; i++) {
    links[i].addEventListener("click", scrollToSection);
  }
});

// Scroll to the section when an anchor link is clicked
function scrollToSection(event) {
  nav_links.classList.toggle("slide");
  event.preventDefault();
  var targetId = event.target.getAttribute("href");
  document.querySelector(".overlay").style.display = "none";
  var targetSection = document.querySelector(targetId);
  targetSection.scrollIntoView({ behavior: "smooth" });
  // animateSection(targetSection);
}

// Apply animation to the section
function animateSection(section) {
  section.classList.add("active");
  section.style.animation = "fadeInUp 0.5s ease";
}
