const openresult = document.querySelector(".result");
const btn_robot = document.querySelector(".chatbot-btn");
const btn_ask = document.querySelector("#ask-btn");
const btn_wait = document.getElementById("wait_btn");
const overlay = document.querySelector(".overlay-wait");
const btn_close_result = document.querySelector(".close-result");

function showLoadingPopup() {
  // Simulate loading process
  setTimeout(function () {
    hideLoadingPopup();
    showDesiredPopup();
  }, 2000); // Adjust the timeout duration as needed
}
function hideLoadingPopup() {
  // overlay.classList.add("hidden");
}
function showDesiredPopup() {
  btn_wait.style.zIndex = 0;
}

//event
btn_robot.addEventListener("click", function () {
  openresult.classList.remove("hidden");
});

btn_ask.addEventListener("click", function (event) {
  event.preventDefault();
  //overlay.classList.remove("hidden");
  btn_wait.style.zIndex = 4;
  showLoadingPopup();
});

btn_close_result.addEventListener("click", function () {
  openresult.classList.add("hidden");
  btn_wait.style.zIndex = 0;
});
