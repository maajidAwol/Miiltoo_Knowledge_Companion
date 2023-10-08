const openresult = document.querySelector(".result");
const openquize = document.querySelector(".quize");
const btn_robot = document.querySelector(".chatbot-btn");
const btn_ask = document.querySelector("#ask-btn");
const btn_wait = document.getElementById("wait_btn");
const overlay = document.querySelector(".overlay-wait");
const btn_generate = document.querySelector(".generete");
const btn_close_result = document.querySelector(".close-result");
const btn_close_quize = document.getElementById("close-quize");
const btn_toggle = document.getElementById("toggle-btn");
const btn_quize = document.getElementById("quizeToggle");
const btn_quize_toggle = document.getElementById("quizeToggle-child");
const toggle_btn_item = document.getElementById("toggle-btn-item");

function showLoadingPopup() {
  // Simulate loading process
  setTimeout(function () {
    hideLoadingPopup();
    showDesiredPopup();
  }, 1500); // Adjust the timeout duration as needed
}
function hideLoadingPopup() {
  overlay.classList.add("hidden");
}
function showDesiredPopup() {
  btn_wait.style.zIndex = 0;
}

//event
btn_robot.addEventListener("click", function () {
  openresult.classList.remove("hidden");
});

btn_toggle.addEventListener("click", function () {
  openresult.classList.add("hidden");
  openquize.classList.remove("hidden");
  btn_quize_toggle.style.backgroundColor = "#0899ff";
  btn_quize_toggle.style.animationDelay = "1";
  toggle_btn_item.style.left = "25px";
});
btn_quize.addEventListener("click", function () {
  openquize.classList.add("hidden");
  openresult.classList.remove("hidden");
});

btn_close_result.addEventListener("click", function () {
  openresult.classList.add("hidden");
  btn_wait.style.zIndex = 0;
});
btn_close_quize.addEventListener("click", function () {
  openquize.classList.add("hidden");
  btn_wait.style.zIndex = 0;
});
