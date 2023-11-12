const chat_btn = document.querySelector("#chat-btn");
const quize_btn = document.querySelector("#quize-btn");
const main_btn = document.querySelectorAll(".chatbot-func-item");
const left_btn = document.querySelectorAll(".chat-left-btn");
const chat_sect = document.querySelector(".chatbot-var-2");
const quize_sect = document.querySelector(".chatbot-var-3");

function stateChanger() {
  const active_shape = document.querySelectorAll(".active-state-shape");

  for (let i = 0; i < main_btn.length; i++) {
    main_btn[i].classList.remove("active");
  }

  event.target.classList.add("active");
  for (let i = 0; i < active_shape.length; i++) {
    if (!active_shape[i].classList.contains("hidden")) {
      active_shape[i].classList.add("hidden");
    }
  }
}

chat_btn.addEventListener("click", () => {
  stateChanger();
  chat_btn.querySelector(".active-state-shape").classList.remove("hidden");
  for (let i = 0; i < main_btn.length; i++) {
    main_btn[i].classList.remove("flashlight");
  }
  chat_btn.classList.add("flashlight");

  if (!quize_sect.classList.contains("hidden")) {
  }
  if (!quize_sect.classList.contains("hidden")) {
    quize_sect.classList.add("hidden");
  }

  chat_sect.classList.remove("hidden");
  collapse_2();

  // Assuming right_arrow_btn is defined somewhere else
  right_arrow_btn.classList.add("hidden");

  for (let i = 0; i < left_btn.length; i++) {
    left_btn[i].classList.toggle("rotate-btn");
  }
});

quize_btn.addEventListener("click", () => {
  stateChanger();
  quize_btn.querySelector(".active-state-shape").classList.remove("hidden");
  for (let i = 0; i < main_btn.length; i++) {
    main_btn[i].classList.remove("flashlight");
  }
  quize_btn.classList.add("flashlight");

  if (!chat_sect.classList.contains("hidden")) {
    chat_sect.classList.add("hidden");
  }

  quize_sect.classList.remove("hidden");
  collapse_2();

  // Assuming right_arrow_btn is defined somewhere else
  right_arrow_btn.classList.add("hidden");

  for (let i = 0; i < left_btn.length; i++) {
    left_btn[i].classList.toggle("rotate-btn");
  }
});

for (let i = 0; i < left_btn.length; i++) {
  left_btn[i].addEventListener("click", () => {
    stateChanger();
    for (let i = 0; i < main_btn.length; i++) {
      main_btn[i].classList.remove("flashlight");
    }
    chat_sect.classList.add("hidden");
    quize_sect.classList.add("hidden");
    console.log("clicke-" + i);
    right_arrow_btn.classList.remove("hidden");
  });
}

const chatbot_headline = document.querySelector(".chatbot-headline");
const chatbot_logo = document.querySelector(".chatbot-logo");
const robot = document.querySelector(".robot-say-hi");
const book_container = document.querySelector(".book-container");
const chatbot_var_1 = document.querySelector(".chatbot-var-1");
const func_container = document.querySelector(".func-container");
const btn_text = document.querySelectorAll(".chatbot-func-item p");
const right_arrow_btn = document.querySelector(".right-arrow-btn");
function collapse() {
  chatbot_logo.classList.toggle("visible");
  right_arrow_btn.classList.toggle("rotate-btn");
  book_container.classList.toggle("toWidth");
  robot.classList.toggle("toPosition");
  chatbot_headline.classList.toggle("toPosition");
  func_container.classList.toggle("toY");
  for (let i = 0; i < btn_text.length; i++) {
    btn_text[i].classList.toggle("minWidth");
  }
  chatbot_var_1.classList.toggle("width");
}
right_arrow_btn.addEventListener("click", () => {
  collapse();
});
function collapse_2() {
  chatbot_logo.classList.add("visible");
  right_arrow_btn.classList.add("rotate-btn");
  book_container.classList.add("toWidth");
  robot.classList.add("toPosition");
  chatbot_headline.classList.add("toPosition");
  func_container.classList.add("toY");
  for (let i = 0; i < btn_text.length; i++) {
    btn_text[i].classList.add("minWidth");
  }
  chatbot_var_1.classList.add("width");
}
const btns = document.querySelectorAll(".btns");
const line_1 = document.querySelector(".float_btn :nth-child(1)");
const line_2 = document.querySelector(".float_btn :nth-child(2)");
const chat_container = document.querySelector(".chat-sec");
let isOpen = false;

chat_container.style.padding = `8px 2%`;

for (let i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", () => {
    btns[i].classList.toggle("open");
    line_1.classList.toggle("open");
    line_2.classList.toggle("open");
    isOpen = !isOpen;

    for (let j = 0; j < btns.length; j++) {
      if (isOpen) {
        btns[j].style.transform = `translateY(${-78 * (j + 1)}px)`;
      } else {
        btns[j].style.transform = `translateY(0px)`;
      }
    }
    if (i == 1) {
      book_container.style.display = "none";
      quize_sect.classList.remove("hidden");
      chat_container.style.padding = `8px 0%`;

      chat_sect.classList.add("hidden");
    } else if (i == 2) {
      book_container.style.display = "none";
      chat_container.style.padding = `8px 0%`;
      chat_sect.classList.remove("hidden");
      quize_sect.classList.add("hidden");
    } else if (i == 3) {
      book_container.style.display = "block";
      chat_container.style.padding = `8px 2%`;
      chat_sect.classList.add("hidden");
      quize_sect.classList.add("hidden");
    } else {
    }
  });
}
