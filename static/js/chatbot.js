const prompt = document.querySelector("#aaa");
const submit = document.querySelector("#bbb");
const response = document.querySelector("#ccc");

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
