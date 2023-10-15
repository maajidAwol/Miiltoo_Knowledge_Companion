function sliderWithAuto(section, item, indicator, left, right, sec_nav) {
  const slider_section = document.querySelector(`${section}`);
  const slide_content = document.querySelectorAll(`${item}`);
  const indicator_container = document.querySelector(`${indicator}`);
  const indicator_dots = document.querySelectorAll(`${indicator} .dots`);
  const left_btn = document.querySelector(`${sec_nav} ${left}`);
  const right_btn = document.querySelector(`${sec_nav} ${right}`);
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
    intervalId = setInterval(slideToNext, 5000); // Adjust the interval duration as needed
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
  ".resource-sec",
  ".resrc-item",
  ".resrc-slider-indicator",
  ".left-btn",
  ".right-btn",
  ".resrc-nav-container"
);
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
