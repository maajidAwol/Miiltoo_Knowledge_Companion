const prompt = document.querySelector("#prompt");
const submit = document.querySelector(".ask");
const response = document.querySelector("#response");

submit.addEventListener("click", function (event) {
 
  event.preventDefault();
  fetch("/request", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ prompt: prompt.value.trim() }),
  })
    .then((response) => response.json())
    .then((data) => {
      res = document.createElement("p");
      res.innerHTML = data.answer;
      response.appendChild(res);
    });
});
