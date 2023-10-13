const slider_testimoney = document.querySelector(".resrc-container");
const slide_content = document.querySelectorAll(".resrc-item");
const testi_indicator_container = document.querySelector(
  ".resrc-slider-indicator"
);
const testi_indicator = document.querySelectorAll(
  ".resrc-slider-indicator .dots"
);
const testi_left_btn = document.querySelector(".left-btn");
const testi_right_btn = document.querySelector(".right-btn");
slide_content.forEach(
  (s, i) => (s.style.transform = `translateX(${100 * i}%)`)
);
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

  testi_indicator.forEach((testi_indicator) => {
    testi_indicator.classList.remove("active");
  });
  const dots = document.querySelector(
    `.resrc-slider-indicator :nth-child(${currentSlide + 1})`
  );
  dots.classList.add("active");
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
  testi_indicator.forEach((testi_indicator) => {
    testi_indicator.classList.remove("active");
  });
  const dots = document.querySelector(
    `.resrc-slider-indicator :nth-child(${currentSlide + 1})`
  );
  dots.classList.add("active");
}

testi_indicator_container.addEventListener("click", function (e) {
  if (e.target.classList.contains("dots")) {
    const { slide } = e.target.dataset;
    slide_content.forEach(
      (s, i) => (s.style.transform = `translateX(${100 * (i - slide)}%)`)
    );
  }
});
const dots = document.querySelectorAll(".dots");
for (let i = 0; i < dots.length; i++) {
  dots[i].addEventListener(".click", () => {
    let n = i;
    slide_content.forEach(
      (s, i) => (s.style.transform = `translateX(${100 * (i - n)}%)`)
    );
  });
}
testi_right_btn.addEventListener("click", slideToNext);
testi_left_btn.addEventListener("click", slideToPrev);
document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowRight") {
    slideToNext();
  }
  e.key === "ArrowLeft" && slideToPrev();
});
