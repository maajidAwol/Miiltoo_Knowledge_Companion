const left_btn = document.querySelector(".left-btn");
const right_btn = document.querySelector(".right-btn");
const resrc_slider = document.querySelector(".resrc-slider");
const resrc_slider_item = document.querySelector(".resrc-container");
const slider = document.getElementById("resrc-container");
const resrc_box = document.querySelectorAll(".resrc-box");
let counter = 1;
let str=``;
function slider_adjust() {
  let netAdd;
  const indicator_container = document.querySelector(".resrc-slider-indicator");
  if (window.matchMedia("(768px <= width < 1200px)").matches) {
    netAdd=(resrc_box.length/2)-3;
    let oldCont=indicator_container.innerHTML;
    for (let i = 0; i < netAdd; i++) {
      console.log(`netAdd-${netAdd}`);
      str += `<span class="dots"></span>`;
      indicator_container.innerHTML = oldCont + str;
    }
  }
  return netAdd;
}
slider_adjust();
const indicator = document.querySelectorAll(".resrc-slider-indicator span");

left_btn.addEventListener("click", () => {
  if(window.matchMedia('(768px <= width < 992px)').matches){
    console.log('young');
    resrc_slider_item.scrollLeft -= (resrc_slider_item.scrollWidth * (2/resrc_box.length));
  }
  else if (window.matchMedia('(width >= 992px)').matches) {
    resrc_slider_item.scrollLeft -= (resrc_slider_item.scrollWidth * (3/resrc_box.length));
  } else {
    
  }
  console.log(`slider--${resrc_slider_item.scrollLeft}`);
 // indicator.length=indicator.length + netAdd;
indicator.forEach(indicator => {
  indicator.classList.remove("active");
  });
  if (counter == 1) {
    counter = indicator.length;
    resrc_slider_item.scrollLeft = resrc_slider_item.scrollWidth;
  } else {
    counter--;
  }
  const dots = document.querySelector(
    `.resrc-slider-indicator :nth-child(${counter})`
  );
  dots.classList.add("active");
  console.log(`clicked-${counter}`);
});
right_btn.addEventListener("click", () => {
  if(window.matchMedia('(768px <= width < 992px)').matches){
    console.log('young');
    resrc_slider_item.scrollLeft += (resrc_slider_item.scrollWidth * (2/resrc_box.length));
  }
  else if (window.matchMedia('(width >= 992px)').matches) {
    resrc_slider_item.scrollLeft += (resrc_slider_item.scrollWidth * (3/resrc_box.length));
  } else {
    
  }
  indicator.forEach((indicator) => {
    indicator.classList.remove("active");
  });
  if (counter == indicator.length) {
    counter = 1;
    resrc_slider_item.scrollLeft = 0;
  } else {
    counter++;
  }
  const dots = document.querySelector(
    `.resrc-slider-indicator :nth-child(${counter})`
  );
  dots.classList.add("active");
  console.log(`clicked-${counter}`);
});
for (let i = 0; i < indicator.length; i++) {
  const slide_ind = indicator[i];
  slide_ind.addEventListener("click", () => {
    indicator.forEach((indicator) => {
      indicator.classList.remove("active");
    });
    slide_ind.classList.add("active");
    let slideWidth = slider.offsetWidth;
    slider.scrollLeft = i * ((resrc_slider_item.scrollWidth * 33.5) / 100);
    counter = i + 1;
  });
}
function wheelPrevent() {
  if (window.matchMedia("(min-width:992px)").matches) {
    resrc_slider_item.addEventListener(
      "wheel",
      (e) => {
        e.preventDefault();
      },
      { passive: false }
    );
  }
}
window.addEventListener("load", () => {
  wheelPrevent();
});
window.addEventListener("resize", () => {
  wheelPrevent();
});


