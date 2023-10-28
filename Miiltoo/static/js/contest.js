let biology_quizData = [];
var biology_score = 0;
var total_point = 0;
var total_question = 0;
const quizContainer = document.getElementById("biology-quiz-container");
const submitButton = document.getElementById("biology-submit-button");
const resultsContainer = document.getElementById("biology-results");
const bio_score = document.getElementById("bio-score");
const history_quizContainer = document.getElementById("history-quiz-container");
const history_submitButton = document.getElementById("history-submit-button");
const history_resultsContainer = document.getElementById("history-results");
let history_quizData = [];
var history_score = 0;
const hist_score = document.getElementById("hist-score");
var total_score = document.getElementById("total-score");
// total-scoreTo store fetched quiz data

const chemistry_quizContainer = document.getElementById(
  "chemistry-quiz-container"
);
const chemistry_submitButton = document.getElementById(
  "chemistry-submit-button"
);
const chemistry_resultsContainer = document.getElementById("chemistry-results");
let chemistry_quizData = [];
var chemistry_score = 0;
const chem_score = document.getElementById("chem-score");
const geography_quizContainer = document.getElementById(
  "geography-quiz-container"
);
const geography_submitButton = document.getElementById(
  "geography-submit-button"
);
const geography_resultsContainer = document.getElementById("geography-results");
let geography_quizData = [];
var geography_score = 0;
const geo_score = document.getElementById("geo-score");

document.addEventListener("DOMContentLoaded", function (event) {
  event.preventDefault();
  submitButton.style.display = "none";

  quizContainer.innerHTML = ""; // Clear the previous quiz content
  resultsContainer.style.display = "none"; // Hide the results
  quizContainer.innerHTML = `

<div class="space-holder" style="height:48px;"></div>
<div class="animation-logo">
<div class="loading-anime">
  <svg
    id="logo"
    width="47"
    height="47"
    viewBox="0 0 47 47"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path
      d="M23.1628 21.5686L23.5001 21.8768L23.8374 21.5686L30.4617 15.5149C30.4784 15.4997 30.5024 15.4958 30.523 15.5048L30.7247 15.0473L30.523 15.5048C30.5436 15.5139 30.5569 15.5343 30.5569 15.5568V19.1273H30.4433V16.82V15.6857L29.606 16.4509L23.5384 21.9957C23.5167 22.0156 23.4834 22.0156 23.4617 21.9957L17.3942 16.4509L16.5569 15.6857V16.82V19.1273H16.4432V15.5568C16.4432 15.5343 16.4565 15.5139 16.4771 15.5048C16.4977 15.4958 16.5218 15.4997 16.5384 15.5149L23.1628 21.5686ZM16.4432 28.3115V25.3773H16.5569V28.1648V28.3584L16.6873 28.5016L16.7105 28.5269C16.7105 28.5269 16.7105 28.527 16.7105 28.527C16.8197 28.6461 16.9793 28.8165 17.1809 29.021C17.5843 29.4302 18.1555 29.9755 18.827 30.5207C19.4986 31.0661 20.2695 31.6103 21.0721 32.0181C21.8751 32.426 22.7064 32.6955 23.5001 32.6955C24.2937 32.6955 25.125 32.426 25.9281 32.0181C26.7307 31.6103 27.5015 31.0661 28.1731 30.5207C28.8446 29.9755 29.4158 29.4302 29.8192 29.021C30.0208 28.8165 30.1805 28.6461 30.2896 28.5269L30.3128 28.5016L30.4433 28.3584V28.1648V25.3773H30.5569V28.3115L30.5001 28.3773L30.1734 28.7558L30.2059 28.7839C30.1189 28.8761 30.0164 28.9828 29.9001 29.1008C29.4947 29.512 28.9203 30.0604 28.2448 30.6089C27.5694 31.1574 26.7917 31.7068 25.9795 32.1194C25.1679 32.5318 24.3183 32.8092 23.5001 32.8092C22.6819 32.8092 21.8323 32.5318 21.0206 32.1194C20.2085 31.7068 19.4308 31.1574 18.7554 30.6089C18.0798 30.0604 17.5054 29.512 17.1 29.1008C16.9837 28.9828 16.8812 28.8761 16.7943 28.7839C16.8048 28.7748 16.8156 28.7654 16.8268 28.7558L16.5001 28.3773L16.4432 28.3115Z"
      stroke="#5CFFFC"
    ></path>
    <path
      d="M16.5 25.1381C18.0941 25.1381 19.3864 23.8458 19.3864 22.2517C19.3864 20.6576 18.0941 19.3653 16.5 19.3653C14.9059 19.3653 13.6136 20.6576 13.6136 22.2517C13.6136 23.8458 14.9059 25.1381 16.5 25.1381ZM19.5 22.2517C19.5 23.9086 18.1569 25.2517 16.5 25.2517C14.8431 25.2517 13.5 23.9086 13.5 22.2517C13.5 20.5949 14.8431 19.2517 16.5 19.2517C18.1569 19.2517 19.5 20.5949 19.5 22.2517Z"
      stroke="#5CFFFC"
    ></path>
    <path
      d="M23.3708 26.3608L23.5001 26.3954L23.6293 26.3608L26.1104 25.6969C26.1407 25.6888 26.1719 25.7068 26.18 25.7371C26.1881 25.7674 26.1701 25.7986 26.1398 25.8067L23.9276 26.3986L23.5569 26.4978V26.8816V32.5538C23.5569 32.5852 23.5315 32.6106 23.5001 32.6106C23.4687 32.6106 23.4433 32.5852 23.4433 32.5538V26.8816V26.4978L23.0725 26.3986L20.8604 25.8067C20.8301 25.7986 20.8121 25.7674 20.8202 25.7371C20.8283 25.7068 20.8594 25.6888 20.8898 25.6969L23.3708 26.3608Z"
      stroke="#5CFFFC"
    ></path>
    <path
      d="M17.375 22.2521C17.375 22.7354 16.9833 23.4316 16.5 23.4316C16.0168 23.4316 15.625 22.7354 15.625 22.2521C15.625 21.7689 16.0168 20.8066 16.5 20.8066C16.9833 20.8066 17.375 21.7689 17.375 22.2521Z"
      fill="#00FFFA"
    ></path>
    <path
      d="M30.5 25.1381C32.0941 25.1381 33.3864 23.8458 33.3864 22.2517C33.3864 20.6576 32.0941 19.3653 30.5 19.3653C28.9059 19.3653 27.6136 20.6576 27.6136 22.2517C27.6136 23.8458 28.9059 25.1381 30.5 25.1381ZM33.5 22.2517C33.5 23.9086 32.1569 25.2517 30.5 25.2517C28.8431 25.2517 27.5 23.9086 27.5 22.2517C27.5 20.5949 28.8431 19.2517 30.5 19.2517C32.1569 19.2517 33.5 20.5949 33.5 22.2517Z"
      stroke="#5CFFFC"
    ></path>
    <path
      d="M31.375 22.2521C31.375 22.7354 30.9833 23.4316 30.5 23.4316C30.0168 23.4316 29.625 22.7354 29.625 22.2521C29.625 21.7689 30.0168 20.8066 30.5 20.8066C30.9833 20.8066 31.375 21.7689 31.375 22.2521Z"
      fill="#00FFFA"
    ></path>
    <path
      d="M23.5 46.5C36.2025 46.5 46.5 36.2025 46.5 23.5C46.5 10.7975 36.2025 0.5 23.5 0.5C10.7975 0.5 0.5 10.7975 0.5 23.5C0.5 36.2025 10.7975 46.5 23.5 46.5ZM44 23.5C44 35.3741 35.3741 44 23.5 44C11.6259 44 3 35.3741 3 23.5C3 11.6259 11.6259 3 23.5 3C35.3741 3 44 11.6259 44 23.5Z"
      stroke="#00FFFA"
    ></path>
  </svg>
</div>
<div class="loader1">
  <span style="--i: 0"></span>
  <span style="--i: 1"></span>
  <span style="--i: 2"></span>
  <span style="--i: 3"></span>
  <span style="--i: 4"></span>
</div>
<div class="loader2">
  <span style="--i: 0"></span>
  <span style="--i: 1"></span>
  <span style="--i: 2"></span>
  <span style="--i: 3"></span>
</div>
</div>
`;
  fetch("/contest_request", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      const load = document.querySelector(".animation-logo");
      const space = document.querySelector(".space-holder");
      load.classList.replace("animation-logo", "hidden");
      space.classList.replace("space-holder", "hidden");

      if (data && data.biology && data.biology.quiz) {
        biology_quizData = data.biology.quiz;
        buildQuiz(quizContainer, biology_quizData);
        history_quizData = data.history.quiz;
        buildQuiz(history_quizContainer, history_quizData);
        //
        chemistry_quizData = data.chemistry.quiz;
        buildQuiz(chemistry_quizContainer, chemistry_quizData);
        //
        geography_quizData = data.geography.quiz;
        buildQuiz(geography_quizContainer, geography_quizData);
        submitButton.style.display = "flex";
      } else {
        // Handle the case where the response is empty or doesn't contain quiz data
        // You can show an error message or take appropriate action here

        quizContainer.innerHTML =
          '<span style="color:red;">error generating quiz please re generate </span>';
        console.error("Empty or invalid response from the server");
        alert("Error: Empty or invalid response from the server");
      }
    })
    .catch((error) => {
      // Handle network errors or other exceptions here
      quizContainer.innerHTML =
        '<span style="color:red;">error generating quiz please re generate </span>';

      console.error("Error fetching data:", error);
      alert("Error fetchinmmg data: " + error.message);
    });

  return false; // Prevent form submission
});

function buildQuiz(quizContainer, quizData) {
  score = 0;

  quizData.forEach((question, index) => {
    const choices = question.choices;
    const questionElement = document.createElement("div");
    questionElement.classList.add("quize-content-container");
    questionElement.innerHTML = `
    <p class="quize-question-container"><span class="quize-no">${
      index + 1
    }</span><span class="quize-question">${question.question}</span></p>`;

    Object.keys(choices).forEach((choice) => {
      const choiceLabel = document.createElement("label");
      choiceLabel.classList.add("quize-choose");
      choiceLabel.innerHTML = `
        <input type="radio" name="question${index}" value="${choice}" required>
       <span class="choose-list"> ${choice}</span>: <p class="choose-item">
               ${choices[choice]}
              </p>
      <br>`;

      questionElement.appendChild(choiceLabel);
    });

    quizContainer.appendChild(questionElement);
    let response_text = document.querySelector(".quize-question");

    //response_text.classList.replace("chatbot-content", "content-afterResponse");
  });

  submitButton.disabled = false;
}

submitButton.addEventListener("click", function () {
  showResults(
    resultsContainer,
    biology_quizData,
    bio_score,
    "Biology",
    biology_score
  );
  submitButton.style.display = "none";
});
history_submitButton.addEventListener("click", function () {
  showResults(
    history_resultsContainer,
    history_quizData,
    hist_score,
    "History",
    history_score
  );
  history_submitButton.style.display = "none";
});
geography_submitButton.addEventListener("click", function () {
  showResults(
    geography_resultsContainer,
    geography_quizData,
    geo_score,
    "Geography",
    geography_score
  );
  geography_submitButton.style.display = "none";
});

chemistry_submitButton.addEventListener("click", function () {
  showResults(
    chemistry_resultsContainer,
    chemistry_quizData,
    chem_score,
    "Chemistry",
    chemistry_score
  );
  chemistry_submitButton.style.display = "none";
  total_score.innerHTML = `           <div class="score-container">
  <div class="score-board">
    Total Score : <span class="score">${total_point}</span><span class="total-quize">/${total_question}</span>
   </div>
 </div><br>`;
});
function showResults(
  resultsContainer,
  quizData,
  score_container,
  title,
  subject_score
) {
  score = 0; // Reset the score before evaluating user answers
  resultsContainer.innerHTML = `
  <div class="result-label2-container">
            <div class="result-line"></div>
            <div class="result-label2">result</div>
           </div>
           <div class="explanation-container">
           <span class="chatbot-icon">
   <img src="/static/asset/logo.svg" alt="">

 </span>
 </div>
           <div class="explanation-label">
            <span class="fether-icon">
              <i class="fa-solid fa-feather"></i>
            </span>
            explanation
          </div>


           `;
  resultsContainer.classList.add("expln-content");

  quizData.forEach((question, index) => {
    const userAnswer = document.querySelector(
      `input[name="question${index}"]:checked`
    );
    const correctAnswer = question.answer;

    if (userAnswer) {
      const userChoice = userAnswer.value;
      if (userChoice === correctAnswer) {
        score++;
      }

      const explanation = question.explanation;
      const resultElement = document.createElement("div");
      resultElement.classList.add("expln-item");

      resultElement.innerHTML = `

        <div class="question-container"><span class="quize-no"><strong>Question ${
          index + 1
        }:</strong></span><p class="question"> ${question.question}</p></div>
       <div class="your-answer">Your answer: ${userChoice}
       <span class="x-icon ${
         userChoice === correctAnswer ? "hidden" : "other"
       }"><i class="fa-solid fa-circle-xmark"></i></span>
       <span class="correct-icon  ${
         userChoice === correctAnswer ? "other" : "hidden"
       } "><i class="fa-solid fa-circle-check"></i></span>
       </div>
         <div class="correct-answer">
           <span class="correct-icon"><i class="fa-solid fa-circle-check"></i></span>
         Correct answer: ${correctAnswer}</div>

         <div class="expln-detail-container">
        <div class="explanation-label expln-detail-label">
        <span class="fether-icon">
          <i class="fa-solid fa-feather"></i>
      </span>
        explanation
    </div>
    <p class="expln-detail">${explanation}
</p>
<div>
        </div>
        </div>
      `;
      resultsContainer.appendChild(resultElement);
    }
  });

  resultsContainer.style.display = "flex";
  //  resultsContainer.innerHTML += `<p>Your score: ${score}/${quizData.length}</p>`;
  resultsContainer.innerHTML += `           <div class="score-container">
            <div class="score-board">
              your score : <span class="score">${score}</span><span class="total-quize">/${quizData.length}</span>
             </div>
           </div><br>`;
  total_question += quizData.length;
  total_point += score;

  score_container.innerHTML = `           <div class="score-container">
  <div class="score-board">
   ${title}  score : <span class="score">${score}</span><span class="total-quize">/${quizData.length}</span>
   </div>
 </div><br>`;
}

//pysics
