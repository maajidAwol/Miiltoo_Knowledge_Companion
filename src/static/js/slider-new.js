const slider_container = document.getElementById("resrc-container");
const dots_container = document.querySelector(".resrc-slider-indicator");

var resrc_btns = document.querySelectorAll(".resrc-btns button");
var grade_btns = document.querySelectorAll(".grade-menu-btn");
var country_menu_btn = document.querySelectorAll(".country-menu-btn");
var grade_no = document.querySelectorAll(".grade_no");
var country_code = "ETH";
let currentImage = 9;
let g_no = 9;
let k = 0;
var subj_Name = [
  "biology",
  "history",
  "citizenship",
  "chemistry",
  "physics",
  "geography",
];

var cover_color = ["#0CABA4", "#1AA751", "#1AA751", "#AA8EC1", "", "#7570B3"];

createResrc(currentImage, country_code, subj_Name, k);
sliderWithAuto(
  ".resource-sec",
  ".resrc-item",
  ".resrc-slider-indicator",
  ".left-btn",
  ".right-btn",
  ".resrc-nav-container"
);
handler(country_code);
function handleCountrySelection(country) {
  const storedCountry = localStorage.getItem("selectedCountry");

  // Check if a selected country is stored
  if (storedCountry) {
    const country = storedCountry.toLowerCase();

    // Update the country button with the selected country
    country_btn.innerHTML = `
    <span class="upload-btn-icon">
    <i class="fa-solid fa-globe"></i>
  </span>
  Country
      <span class="country-menu-item-icon" style='display: flex;
        justify-content: center;
        align-items: center;
        gap: 4px;'>
        <img src="/static/asset/${country}-flag.svg" alt="" />
      </span>
    `;

    // Update the content and handle the selected country
    changeContent(country, null);
  }
}
function changeContent(country, event) {
  event.preventDefault();

  if (country === "ethiopia") {
    country_code = "ETH";
    cover_color = ["#3D996A", "#EE1D23", "#CF6E65", "#AA8EC1", "", "#7570B3"];
  } else if (country === "nigeria") {
    country_code = "NGA";
  } else if (country === "kenya") {
    country_code = "KEN";
    newContent = "Content for Kenya";
  } else if (country === "south-sudan") {
    country_code = "SS";
    cover_color = ["#3D996A", "#EE1D23", "#CF6E65", "#AA8EC1", "", "#7570B3"];
  }
  var country_btn = document.getElementById("country-btn");

  country_btn.innerHTML = `
  <span class="upload-btn-icon">
  <i class="fa-solid fa-globe"></i>
</span>
Country
    <span class="country-menu-item-icon" style='display: flex;
      justify-content: center;
      align-items: center;
      gap: 4px;'>
      <img src="/static/asset/${country}-flag.svg" alt="" />
    </span>
`;
  // if (window.matchMedia("(width < 992px)").matches) {
  //   document.querySelector(".nav-links").classList.toggle("slide");
  //   document.querySelector(".overlayHeader").classList.toggle("hidden");
  //   document.querySelector(".hamb-menu").classList.toggle("active");
  // }
  slider_container.innerHTML = ``;
  dots_container.innerHTML = ``;
  createResrc(9, country_code, subj_Name, k);
  sliderWithAuto(
    ".resource-sec",
    ".resrc-item",
    ".resrc-slider-indicator",
    ".left-btn",
    ".right-btn",
    ".resrc-nav-container"
  );
  handler(country_code);
}

function handler(country_code) {
  for (let i = 0; i < grade_btns.length; i++) {
    grade_btns[i].addEventListener("click", function (event) {
      slider_container.innerHTML = ``;
      dots_container.innerHTML = ``;
      grade_menu.classList.remove("hidden");
      // event.stopPropagation()
      if (window.matchMedia("(width < 992px)").matches) {
        document.querySelector(".nav-links").classList.toggle("slide");
        document.querySelector(".overlayHeader").classList.toggle("hidden");
        document.querySelector(".hamb-menu").classList.toggle("active");
      }
      for (let j = 0; j < resrc_btns.length; j++) {
        resrc_btns[j].classList.replace("active-btn", "other-btns");
      }
      resrc_btns[i + 1].classList.replace("other-btns", "active-btn");
      for (let j = 0; j < grade_no.length; j++) {
        grade_no[j].innerHTML = `grade-${i + 9}`;
      }
      console.log("code-" + country_code);

      currentImage = i + 9;

      createResrc(currentImage, country_code, subj_Name, k);
      sliderWithAuto(
        ".resource-sec",
        ".resrc-item",
        ".resrc-slider-indicator",
        ".left-btn",
        ".right-btn",
        ".resrc-nav-container"
      );
    });
  }
  for (let i = 0; i < resrc_btns.length; i++) {
    resrc_btns[i].addEventListener("click", function () {
      slider_container.innerHTML = ``;
      dots_container.innerHTML = ``;

      for (let j = 0; j < resrc_btns.length; j++) {
        resrc_btns[j].classList.replace("active-btn", "other-btns");
      }
      resrc_btns[i].classList.replace("other-btns", "active-btn");
      for (let j = 0; j < grade_no.length; j++) {
        grade_no[j].innerHTML = `grade-${i + 8}`;
      }
      if (i == 0) {
        currentImage = 9;
      } else {
        currentImage = i + 8;
      }
      createResrc(currentImage, country_code, subj_Name, k);
      sliderWithAuto(
        ".resource-sec",
        ".resrc-item",
        ".resrc-slider-indicator",
        ".left-btn",
        ".right-btn",
        ".resrc-nav-container"
      );
    });
  }
}
window.addEventListener("resize", () => {
  // location.reload();
});
function createResrc(g_no, country_code, subj_Name, k) {
  let length = 0;
  const mediaFor_mob = window.matchMedia("(width < 768px)");
  const mediaFor_tab = window.matchMedia("(768px <= width < 992px)");
  const mediaFor_lap = window.matchMedia("(992px <= width)");
  let p = 0;
  let q = 0;
  if (mediaFor_tab.matches) {
    p = 2;
  } else if (mediaFor_lap.matches) {
    p = 3;
    q = 1;
    if (subj_Name.length % p == 0) {
      q = 0;
    }
  } else {
    // location.reload();
    p = 1;
    q = 1;
    if (subj_Name.length % p == 0) {
      q = 0;
    }
  }
  length = p;
  for (let i = 0; i < q + Math.floor(subj_Name.length / p); i++) {
    slider_container.insertAdjacentHTML(
      "beforeend",
      `  <div class="resrc-item"></div>`
    );
    if (i == 1) {
      let dots = document.querySelector(".dots");
      dots.classList.add("active");
    }
    if (i == q + Math.floor(subj_Name.length / p) - 1) {
      let item = document.querySelectorAll(".resrc-item");
      item[i].classList.toggle("last");
    }
    dots_container.insertAdjacentHTML(
      "beforeend",
      `  <span class="dots"></span>`
    );
  }
  var item_container = document.querySelectorAll(".resrc-item");
  let left_length = subj_Name.length - p * Math.floor(subj_Name.length / p);
  let diff = p - left_length;

  for (let i = 0; i < item_container.length; i++) {
    for (let j = 0; j < length; j++) {
      if (
        left_length > 0 &&
        i == item_container.length - 1 &&
        j > left_length - 1
      ) {
        k = 0;
      }
      // href="/grade/?book=bk/${country_code}/${subj_Name[k]}_g-${g_no}.pdf"

      item_container[i].insertAdjacentHTML(
        "beforeend",
        ` 

<a
href="/grade/?book=bk/${country_code}/${subj_Name[k]}_g-${g_no}.pdf"
class="resrc-box"
>
<div class="resrc-cover-container" style="background:${cover_color[k]};">
  <img
    src="/static/asset/book-cover/${country_code}/${
          subj_Name[k]
        }-g${g_no}-cover.svg"
    class="resrc-cover-item"
  />
  <div class="resrc-cover-overlay">
    <p class='grade_no'>grade-${g_no}</p>
    <span class="resrc-cover-overlay-icon">
      <i class="fa-solid fa-book-open-reader"></i>
    </span>
  </div>
</div>
<div class="resrc-tittle-container">
  <span class="resrc-tittle-icon"
    ><i class="fa-solid fa-book"></i
  ></span>
  ${subj_Name[k++]}
</div>
<div class="resrc-desc-container">
  <div class="resrc-desc-tittle">
    <span class="resc-desc-tittle-icon"
      ><i class="fa-solid fa-feather"></i
    ></span>
    description
  </div>
  <div class="resrc-desc-content">
    <p class="resrc-desc-text">
      ensures that students have access to comprehensive learning
      materials that support their academic progress.
    </p>
  </div>
</div>
</a>
`
      );
    }
  }
}
function sliderWithAuto(section, item, indicator, left, right, sec_nav) {
  const slider_section = document.querySelector(`${section}`);
  const slide_content = document.querySelectorAll(`${item}`);
  const indicator_container = document.querySelector(`${indicator}`);
  const indicator_dots = document.querySelectorAll(`${indicator} .dots`);
  const left_btn = document.querySelector(`${sec_nav} ${left}`);
  const right_btn = document.querySelector(`${sec_nav} ${right}`);
  if (window.matchMedia("(width<600px)").matches) {
    slide_content.forEach((s) => (s.style.transform = `none`));
  } else {
    slide_content.forEach(
      (s, i) => (s.style.transform = `translateX(${100 * i}%)`)
    );
  }
  let currentSlide = 0;
  const maxSlide = slide_content.length - 1;

  function slideToNext() {
    if (currentSlide === maxSlide) {
      currentSlide = 0;
    } else {
      currentSlide++;
    }
    slide_content.forEach(
      (s, i) => (s.style.transform = `translateX(${100 * (i - currentSlide)}%)`)
    );
    slide_content.forEach((slide_content) => {
      if (slide_content.style.transform !== "translateX(0%)") {
        slide_content.style.opacity = 0.6;
      } else {
        slide_content.style.opacity = 1;
      }
    });

    indicator_dots.forEach((indicator_dots) => {
      indicator_dots.classList.remove("active");
    });
    const dots = document.querySelector(
      `${indicator} :nth-child(${currentSlide + 1})`
    );
    dots.classList.add("active");
    if (slider_section !== document.querySelector(".resource-sec")) {
      stopAutoSlide();
    }
  }
  function slideToPrev() {
    if (currentSlide === 0) {
      currentSlide = maxSlide;
    } else {
      currentSlide--;
    }

    slide_content.forEach(
      (s, i) => (s.style.transform = `translateX(${100 * (i - currentSlide)}%)`)
    );
    slide_content.forEach((slide_content) => {
      if (slide_content.style.transform !== "translateX(0%)") {
        slide_content.style.opacity = 0.6;
      } else {
        slide_content.style.opacity = 1;
      }
    });
    indicator_dots.forEach((indicator_dots) => {
      indicator_dots.classList.remove("active");
    });
    const dots = document.querySelector(
      `${indicator} :nth-child(${currentSlide + 1})`
    );
    dots.classList.add("active");
    if (slider_section !== document.querySelector(".resource-sec")) {
      stopAutoSlide();
    }
  }
  let intervalId;

  function startAutoSlide() {
    intervalId = setInterval(slideToNext, 8000); // Adjust the interval duration as needed
  }
  function stopAutoSlide() {
    clearInterval(intervalId);
    startAutoSlide(); // Restart auto-slide timer
  }
  if (slider_section !== document.querySelector(".resource-sec")) {
    startAutoSlide();
  }
  indicator_container.addEventListener("click", function (e) {
    if (e.target.classList.contains("dots")) {
      const { slide } = e.target.dataset;
      slide_content.forEach(
        (s, i) => (s.style.transform = `translateX(${100 * (i - slide)}%)`)
      );
    }
  });
  // const dots = document.querySelectorAll(".dots");
  // for (let i = 0; i < dots.length; i++) {
  //   dots[i].addEventListener(".click", () => {
  //     let n = i;
  //     slide_content.forEach(
  //       (s, i) => (s.style.transform = `translateX(${100 * (i - n)}%)`)
  //     );
  //   });
  // }
  right_btn.addEventListener("click", slideToNext);
  left_btn.addEventListener("click", slideToPrev);
  document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight") {
      slideToNext();
    }
    e.key === "ArrowLeft" && slideToPrev();
  });
}

sliderWithAuto(
  ".testimoney-sec",
  ".person-item",
  ".testi-slider-indicator",
  ".left-btn",
  ".right-btn",
  ".testi-nav-container"
);
sliderWithAuto(
  ".team-sec",
  ".team-member",
  ".team-slider-indicator",
  ".left-btn",
  ".right-btn",
  ".team-nav-container"
);
