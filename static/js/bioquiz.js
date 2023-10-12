const fetchQuizButton = document.getElementById("fetch-quiz");
const quizContainer = document.getElementById("quiz-container");
const submitButton = document.getElementById("submit-button");
const resultsContainer = document.getElementById("results");
const bk_choice = document.getElementById("book_choice");

let quizData = []; // To store fetched quiz data
let score = 0;
fetchQuizButton.addEventListener("click", function (event) {
  event.preventDefault();
  submitButton.style.display = "none";
  fetchQuizButton.style.display = "none";
  quizContainer.innerHTML = ""; // Clear the previous quiz content
  resultsContainer.style.display = "none"; // Hide the results

  fetch("/quiz_request", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      chapter: document.getElementById("chapter").value,
      subtopic: document.getElementById("subtopic").value,
      number: document.getElementById("number").value,
      book_choice: document.getElementById("book_choice").value,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => {
      if (data && data.quiz) {
        quizData = data.quiz;
        buildQuiz();
        submitButton.style.display = "block";
        fetchQuizButton.style.display = "block";
      } else {
        // Handle the case where the response is empty or doesn't contain quiz data
        // You can show an error message or take appropriate action here
        fetchQuizButton.style.display = "block";
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

      fetchQuizButton.style.display = "block";
      console.error("Error fetching data:", error);
      alert("Error fetchinmmg data: " + error.message);
    });

  return false; // Prevent form submission
});

function buildQuiz() {
  score = 0;

  quizData.forEach((question, index) => {
    const choices = question.choices;
    const questionElement = document.createElement("div");
    questionElement.classList.add("quize-content-container");
    questionElement.innerHTML = `
    <p class="quize-question-container"><span class="quize-no">${
      index + 1
    }</span><span class="quize-question"> ${question.question}</span></p>`;

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
  });

  submitButton.disabled = false;
}

submitButton.addEventListener("click", function () {
  showResults();
  submitButton.style.display = "none";
});

function showResults() {
  score = 0; // Reset the score before evaluating user answers
  resultsContainer.innerHTML = ` 
  <div class="result-label2-container">
            <div class="result-line"></div>
            <div class="result-label2">result</div>
           </div>

           <div class="explanation-label">
            <span class="fether-icon">
              <i class="fa-solid fa-feather"></i>
            </span>
            explanation
          </div>
                      <span class="chatbot-icon">
              <img src="/static/asset/logo.svg" alt="">

            </span>
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
        <div class="expln-detail">Explanation: ${explanation}</div>
      `;
      resultsContainer.appendChild(resultElement);
    }
  });

  resultsContainer.style.display = "block";
  //  resultsContainer.innerHTML += `<p>Your score: ${score}/${quizData.length}</p>`;
  resultsContainer.innerHTML += `           <div class="score-container">
            <div class="score-board">
              your score : <span class="score">${score}</span><span class="total-quize">/${quizData.length}</span>
             </div>
           </div><br>`;
}
//var biology = {
//  "chapter 1:Introduction to Biology": {
//    "1.1:Definition of Biology ": [],
//    "1.2:Why do we study Biology?": [],
//    "1.3:The scientific method": [],
//    "1.4:Tools of a Biologist": [],
//    "1.5: Handling and using of light Microscope ": [],
//    "1.6:General Laboratory Safety Rules": [],
//  },
//  "chapter 2:Characteristics and Classification of organisms": {
//    "2.1: Characteristics of living things": [],
//    "2.2: Taxonomy of living things": [],
//    "2.3: Relevance of classification": [],
//    "2.4: Linnaean system of nomenclature": [],
//    "2.5: Common Ethiopian animals and plants": [],
//    "2.6: The five-kingdom system of classification": [],
//    "2.7: Renowned taxonomists in Ethiopia": [],
//  },
//  "chapter 3: Cells": {
//    "3.1: What is a cell?": [],
//    "3.2: Cell theory": [],
//    "3.3: Cell structure and function": [],
//    "3.4: Types of cells": [],
//    "3.5: Animal and plant cells": [],
//    "3.6: Observing cells under a microscope": [],
//    "3.7: The cell and its environment": [],
//    "3.8: Levels of Biological Organization": [],
//  },
//  "chapter 4 :Reproduction": {
//    "4.1: Introduction to reproduction": [],
//    "4.2: Asexual reproduction": [],
//    "4.3: Types of asexual reproduction ": [],
//    "4.4: Sexual reproduction": [],
//    "4.5: Primary and secondary sexual characteristics": [],
//    "4.6: Male reproductive structures": [],
//    "4.7: Female reproductive structures": [],
//    "4.8: The Menstrual cycle": [],
//    "4.9: Fertilization and pregnancy": [],
//    "4.10: Methods of birth control": [],
//    "4.11: Sexually transmitted infection: transmission and prevention": [],
//  },
//  "chapter 5:Human Health, Nutrition, and Disease ": {
//    "5.1: What is food?": [],
//    "5.2: Nutrition": [],
//    "5.3: Nutrients ": [],
//    "5.4: Balanced diet": [],
//    "5.5: Deficiency diseases": [],
//    "5.6: Malnutrition": [],
//    "5.7: Substance abuse ": [],
//    "5.8: Types of diseases": [],
//    "5.9: Renowned Nutritionists in Ethiopia": [],
//  },
//  "chapter 6:Ecology": {
//    "6.1: Ecology": [],
//    "6.2: Ecological relationships": [],
//  },
//};

var ado = document.getElementById("book_choice");
//alert(ado);
window.onload = function () {
  var chapter = document.getElementById("chapter");
  var section = document.getElementById("subtopic");
  var question = document.getElementById("question");
  for (var i in biology) {
    chapter.options[chapter.options.length] = new Option(i);
  }
  chapter.onchange = function () {
    section.length = 1;
    for (var j in biology[this.value]) {
      section.options[section.options.length] = new Option(j);
    }
  };
};
