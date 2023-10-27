//const fetchQuizButton = document.getElementById("fetch-quiz");
//    const quizContainer = document.getElementById('quiz-container');
//    const submitButton = document.getElementById('submit-button');
//    const resultsContainer = document.getElementById('results');
//
//    let quizData; // To store fetched quiz data
//    let score = 0;
//
//    fetchQuizButton.addEventListener("click", function (event) {
//    event.preventDefault();
//      submitButton.style.display = "none";
//      fetchQuizButton.style.display = "none";
//      quizContainer.innerHTML = ''; // Clear the previous quiz content
//      resultsContainer.style.display = "none"; // Hide the results
//
//      fetch("/quiz_requestH", {
//        method: "POST",
//        headers: {
//          "Content-Type": "application/json",
//        },
//        body: JSON.stringify({
//          chapter: document.getElementById("chapter").value,
//          subtopic: document.getElementById("subtopic").value,
//          number: document.getElementById("number").value,
//        }),
//      })
//        .then((response) => response.json())
//        .then((data) => {
//          quizData = data.quiz;
//          buildQuiz();
//          submitButton.style.display = "block";
//          fetchQuizButton.style.display = "block";
//        });
//    });
const fetchQuizButton = document.getElementById("fetch-quiz");
const quizContainer = document.getElementById('quiz-container');
const submitButton = document.getElementById('submit-button');
const resultsContainer = document.getElementById('results');

let quizData; // To store fetched quiz data
let score = 0;

fetchQuizButton.addEventListener("click", function (event) {
  event.preventDefault();
  submitButton.style.display = "none";
  fetchQuizButton.style.display = "none";
  quizContainer.innerHTML = ''; // Clear the previous quiz content
  resultsContainer.style.display = "none"; // Hide the results

  fetch("/quiz_requestH", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      chapter: document.getElementById("chapter").value,
      subtopic: document.getElementById("subtopic").value,
      number: document.getElementById("number").value,
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
      quizContainer.innerHTML = '<span style="color:red;">error generating quiz, please try again</span>';
      console.error("Empty or invalid response from the server");
    }
  })
  .catch((error) => {
    // Handle network errors or other exceptions here
    fetchQuizButton.style.display = "block";
    quizContainer.innerHTML = '<span style="color:red;">error fetching data, please try again</span>';
    console.error("Error fetching data:", error);
  });

  return false; // Prevent form submission
});

    function buildQuiz() {
      score = 0;

      quizData.forEach((question, index) => {
        const choices = question.choices;
        const questionElement = document.createElement('div');
        questionElement.innerHTML = `<p>${index + 1}. ${question.question}</p>`;

        Object.keys(choices).forEach(choice => {
          const choiceLabel = document.createElement('label');
          choiceLabel.innerHTML = `
            <input type="radio" name="question${index}" value="${choice}" required>
            ${choice}: ${choices[choice]}
          <br>`;
          questionElement.appendChild(choiceLabel);
        });

        quizContainer.appendChild(questionElement);
      });

      submitButton.disabled = false;
    }

    submitButton.addEventListener('click', function () {
      showResults();
      submitButton.style.display = "none";
    });

    function showResults() {
      score = 0; // Reset the score before evaluating user answers
      resultsContainer.innerHTML = ''; // Clear previous results

      quizData.forEach((question, index) => {
        const userAnswer = document.querySelector(`input[name="question${index}"]:checked`);
        const correctAnswer = question.answer;

        if (userAnswer) {
          const userChoice = userAnswer.value;
          if (userChoice === correctAnswer) {
            score++;
          }

          const explanation = question.explanation;
          const resultElement = document.createElement('div');
          resultElement.innerHTML = `
            <p><strong>Question ${index + 1}:</strong> ${question.question}</p>
            <p>Your answer: ${userChoice}</p>
            <p>Correct answer: ${correctAnswer}</p>
            <p>Explanation: ${explanation}</p>
          `;
          resultsContainer.appendChild(resultElement);
        }
      });

      resultsContainer.style.display = 'block';
      resultsContainer.innerHTML += `<p>Your score: ${score}/${quizData.length}</p>`;
    }
    let history = {
        "chapter 1: The Discipline of History and Human Evolution": {
        "1.1: Meaning of Prehistory and History": [],
        "1.2: The Discipline of History": [],
        "1.3: The Evolution of Human Beings": [],
        "1.4: Theories of Human Evolution": [],
        "1.5: Africa and Human Evolution": [],
        "1.6: The Stone Age": [],
        "1.7: The Emergence of States": [],
      },
      "chapter 2: Ancient World Civilizations up to c. 500 AD": {
        "2.1: Ancient Civilizations of Africa": [],
        "2.2: Civilizations in Asia": [],
        "2.3: Ancient Civilization of Latin America": [],
        "2.4: Civilizations in Europe": [],
        "2.5: Rise and spread of Christianity": [],
      },
      "chapter 3: Peoples and States in Ethiopia and the Horn to the end of 13th C.": {
        "3.1: Languages, Religions and Peoples of Ethiopia and the Horn": [],
        "3.2: Pre-Aksumite States and their Geographical Setting": [],
        "3.3: Aksumite Kingdom": [],
        "3.4: Zagwe Dynasty": [],
        "3.5: The Sultanate Shewa": [],
      },
      "chapter 4: The Middle Ages and Early Modern World C. 500 to 1750s": {
        "4.1: The Middle Ages in Europe": [],
        "4.2: The Middle Ages in Asia": [],
        "4.3: Development of Early Capitalism": [],
        "4.4: The Age of Explorations and Discoveries": [],
        "4.5: The Renaissance": [],
        "4.6: The Reformation": [],
        "4.7: Industrial Revolution": [],
      },
      "chapter 5: Peoples and States of Africa to 1500": {
        "5.1: Languages and Peoples of Africa": [],
        "5.2: States in North Africa": [],
        "5.3: Spread of Islam and its Impact in West Africa": [],
        "5.4: States in Western Africa": [],
        "5.5: Equatorial, Central and Eastern Africa": [],
        "5.6: Southern Africa": [],
        "5.7: Africa’s Intra and Inter-continental Relations": [],
        "5.8: Trans-Saharan trade": [],
        "5.9: Early Contacts with the Outside World": [],
      },
      "chapter 6: Africa and the Outside World 1500- 1880s": {
        "6.1: Contact with the Outside World": [],
        "6.2: Slavery": [],
        "6.3: The “Legitimate” Trade": [],
        "6.4: The White Settlement in South Africa": [],
        "6.5: European Explorers and Missionaries": [],
      },
      "chapter 7: States, Principalities, Population Movements & Interactions in Ethiopia 13th to Mid-16th C.": {
        "7.1: The “Solomonic” Dynasty & the Christian Kingdom, 13th -16th C": [],
        "7.2: The Muslim Principalities": [],
        "7.3: Relationship Between the Christian Kingdom and the Sultanate of Adal, 1520s to 1559": [],
        "7.4: Political and socio-economic conditions of southern and central states in Ethiopia": [],
        "7.5: Population Movements, Expansion and Integration in Ethiopia": [],
        "7.6: Gada System of the Oromo": [],
        "7.7: Moggasa and Guddifacha": [],
        "7.8: Egalitarian System of Governance": [],
      },
       "chapter 8: Political, Social and Economic Processes in Ethiopia Mid- 16th to Mid- 19thC.": {
        "8.1: Peoples and states of the Eastern, Central, Southern and Western Regions": [],
        "8.2: Gondarine Period": [],
        "8.3: The Zemene Mesafint (The Era of Warlords)": [],
        "8.4: The Yejju Dynasty": [],
        "8.5: The Kingdom of Shoa": [],
      },
      "chapter 9: The Age of Revolutions 1750s to 1815": {
        "9.1: Industrial Capitalism in Europe": [],
        "9.2: French Revolution": [],
        "9.3: Napoleonic Era": [],
        "9.4: American War of Independence": [],
        "9.5: The Congress of Vienna": [],
      },
    };
    
        
        window.onload = function () {
          var chapter = document.getElementById("chapter");
          var section = document.getElementById("subtopic");
          var question = document.getElementById("question");
          for (var i in history) {
            chapter.options[chapter.options.length] = new Option(i);
          }
          chapter.onchange = function () {
            section.length = 1;
            for (var j in history[this.value]) {
              section.options[section.options.length] = new Option(j);
            }
          };
        };