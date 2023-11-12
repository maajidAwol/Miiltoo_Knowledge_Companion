const home_link = document.querySelectorAll(".home-link");
const underline = document.getElementById("underline");
const grade_menu = document.querySelector(".grade-menu");
const grade_menuId = document.getElementById("grade-menu");
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
const overlayHeader = document.querySelector(".overlayHeader");
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
if (window.matchMedia("(min-width:992px)").matches) {
  for (let i = 0; i < home_link.length; i++) {
    home_link[i].addEventListener("mouseover", () => {
      if (i === 0) {
        n = 43 * i;
        currentPosition = 0;
        grade_menu.classList.add("hidden");
        profile_menu.classList.add("hidden");
        page_menu.classList.add("hidden");
        country_menu.classList.add("hidden");
        grade_btn_icon[i].style.transform = "rotate(0deg)";
        profile_drop_icon.style.transform = "rotate(0deg)";
      } else if (i === 1) {
        n = 73 * i;
        grade_menu.classList.remove("hidden");

        profile_menu.classList.add("hidden");
        page_menu.classList.add("hidden");
        country_menu.classList.add("hidden");
        grade_btn_icon[i].style.transform = "rotate(180deg)";
        profile_drop_icon.style.transform = "rotate(0deg)";
        currentPosition = i;
      } else if (i === 2) {
        n = 90 * i;
        currentPosition = i;
        grade_menu.classList.add("hidden");
        profile_menu.classList.add("hidden");
        page_menu.classList.add("hidden");
        country_menu.classList.add("hidden");
        grade_btn_icon[i].style.transform = "rotate(0deg)";
        profile_drop_icon.style.transform = "rotate(0deg)";
      } else if (i === 3) {
        n = 94 * i;
        page_menu.classList.remove("hidden");

        currentPosition = i;
        country_menu.classList.add("hidden");
        profile_menu.classList.add("hidden");
        grade_menu.classList.add("hidden");
        grade_btn_icon[i - 2].style.transform = "rotate(180deg)";
        profile_drop_icon.style.transform = "rotate(0deg)";
      } else {
        n = 0;
        country_menu.classList.remove("hidden");

        currentPosition = i;
        page_menu.classList.add("hidden");
        grade_menu.classList.add("hidden");
        profile_menu.classList.add("hidden");
        grade_btn_icon[i - 2].style.transform = "rotate(180deg)";
        profile_drop_icon.style.transform = "rotate(0deg)";
      }
      // underline.style.transform = `translateX(${n}px)`;
    });
  }
} else {
  for (let i = 0; i < home_link.length; i++) {
    home_link[i].addEventListener("click", function (event) {
      if (i == 1 || i == 3 || i == 4) {
        event.preventDefault();
        event.stopPropagation();
      }
      if (i === 1) {
        grade_menu.classList.toggle("hidden");
        profile_menu.classList.add("hidden");
        page_menu.classList.add("hidden");
        country_menu.classList.add("hidden");
        grade_btn_icon[1].classList.toggle("rotate");
        // profile_drop_icon.style.transform = "rotate(0deg)";
      } else if (i === 3) {
        page_menu.classList.toggle("hidden");
        country_menu.classList.add("hidden");
        profile_menu.classList.add("hidden");
        grade_menu.classList.add("hidden");
        // grade_btn_icon[2].classList.toggle("rotate");
        // profile_drop_icon.style.transform = "rotate(0deg)";
      } else if (i == 4) {
        country_menu.classList.toggle("hidden");
        page_menu.classList.add("hidden");
        grade_menu.classList.add("hidden");
        profile_menu.classList.add("hidden");
      }
    });
  }
}
var html = document.querySelector(".html");
hamb_btn.addEventListener("click", function () {
  nav_links.classList.toggle("slide");
  hamb_btn.classList.toggle("active");
  overlayHeader.classList.toggle("hidden");
  // upload_popup.classList.add("hidden");
  overlayHeader.style.zIndex = "1";
  html.classList.toggle("overflow");
});
overlayHeader.addEventListener("click", () => {
  nav_links.classList.toggle("slide");
  hamb_btn.classList.toggle("active");
  overlayHeader.classList.toggle("hidden");
  overlayHeader.classList.toggle("forMob");
  overlayHeader.style.zIndex = "0";
  overlayHeader.classList.add("hidden");
  upload_popup.classList.add("hidden");
  document.querySelector(".body").style.overflowY = "auto";
  overlay.classList.remove("forMob");
  html.classList.toggle("overflow");
});
if (window.matchMedia("(width>=992px)").matches) {
  profile_group.addEventListener("mouseover", () => {
    profile_menu.classList.remove("hidden");
    grade_menu.classList.add("hidden");
    page_menu.classList.add("hidden");
    country_menu.classList.add("hidden");
    grade_btn_icon.style.transform = "rotate(0deg)";
    profile_drop_icon.style.transform = "rotate(180deg)";
  });
} else {
  profile_group.addEventListener("click", (e) => {
    e.stopPropagation();
    profile_menu.classList.toggle("hidden");
    console.log("cllllllll");
    grade_menu.classList.toggle("hidden");
    page_menu.classList.toggle("hidden");
    country_menu.classList.toggle("hidden");
    // grade_btn_icon.style.transform = "rotate(0deg)";
    profile_drop_icon.style.transform = "rotate(180deg)";
  });
}
uploadFunc();
function uploadFunc() {
  upload_btn.addEventListener("click", (e) => {
    e.preventDefault();
    upload_popup.classList.toggle("hidden");
    if (!window.matchMedia("(width < 992px)").matches) {
      overlayHeader.classList.toggle("hidden");
    }
    overlayHeader.style.zIndex = "2";
    // overlay.classList.toggle("hidden");
    document.querySelector(".body").style.overflowY = "hidden";
    // overlay.classList.remove("forMob");
    // overlay.style.zIndex = "3";
  });
}
close_btn.addEventListener("click", () => {
  overlayHeader.classList.toggle("hidden");
  upload_popup.classList.add("hidden");
  document.querySelector(".body").style.overflowY = "auto";
  overlay.classList.remove("forMob");
});
overlay.addEventListener("click", () => {});

// var mediaQuery = window.matchMedia("(min-width: 768px)");
// if (mediaQuery.matches) {
//   hamb_btn.classList.toggle("hidden");
// }

window.addEventListener("load", function () {
  // window.scrollTo(0, 0);
});
// Add event listeners to anchor links
document.addEventListener("DOMContentLoaded", function () {
  var links = document.querySelectorAll('a[href^="#"]');
  for (var i = 0; i < links.length; i++) {
    links[i].addEventListener("click", scrollToSection);
  }
});
var links = document.querySelectorAll(".page-menu-item");

for (var i = 0; i < links.length; i++) {
  links[i].addEventListener("click", () => {
    if (window.matchMedia("(width < 992px )").matches) {
      // location.reload();

      document.querySelector(".nav-links").classList.toggle("slide");
      document.querySelector(".overlayHeader").classList.toggle("hidden");
      document.querySelector(".hamb-menu").classList.toggle("active");
    }
  });
}

// Scroll to the section when an anchor link is clicked

function scrollToSection(event) {
  // Hide nav links and overlay for screens with width < 992px

  // event.preventDefault();

  var targetId = event.target.getAttribute("href");
  var targetSection = document.querySelector(targetId);

  // Scroll to the target section
  targetSection.scrollIntoView({ behavior: "smooth" });
}
// Apply animation to the section
function animateSection(section) {
  section.classList.add("active");
  section.style.animation = "fadeInUp 0.5s ease";
}

const linkAn = document.querySelectorAll(".link-container");
const linkContainers = document.querySelectorAll(".link-container-inner");
const linkContainers_icon = document.querySelectorAll(
  ".link-container-inner i"
);
const sm_links = document.querySelectorAll(".inner-link");
for (let i = 0; i < linkContainers.length; i++) {
  linkContainers[i].addEventListener("click", (e) => {
    if (!linkAn[i].classList.contains("active")) {
      e.stopPropagation();
      linkAn[i].classList.toggle("active");
      for (let j = 0; j < sm_links.length; j++) {
        if (sm_links[j].classList.contains("show")) {
          sm_links[j].classList.remove("show");
          linkAn[j].style.background = `transparent`;
          linkContainers_icon[j].style.transform = `rotate(0deg)`;
        }
      }
      linkContainers_icon[i].style.transform = `rotate(180deg)`;
      linkAn[i].style.background = `#1e206f3b`;
      sm_links[i].classList.toggle("show");
    } else {
      console.log("cccccc");
      linkAn[i].classList.toggle("active");
      sm_links[i].classList.toggle("show");
      for (let j = 0; j < sm_links.length; j++) {
        // if (sm_links[j].classList.contains("show")) {
        sm_links[j].classList.remove("show");
        linkAn[j].style.background = `transparent`;
        linkContainers_icon[j].style.transform = `rotate(0deg)`;
        // }
      }
    }
  });
}
