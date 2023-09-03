// const prompt = document.querySelector("#aaa");
// const submit = document.querySelector("#bbb");
// const response = document.querySelector("#ccc");

// submit.addEventListener("click", function (event) {


//   event.preventDefault();
//   fetch("/request", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({ prompt: prompt.value.trim() }),
//   })
//     .then((response) => response.json())
//     .then((data) => {
//       res = document.createElement("p");
//       res.innerHTML = data.answer;
//       response.appendChild(res);
//     });
// });
const chatBox = document.querySelector("#ccc");
const messageInput = document.querySelector("#aaa");
const sendBtn = document.querySelector("#bbb");

function addMessage(message, isUserMessage) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("mt-3", "p-3", "rounded");

  if (isUserMessage) {
    messageDiv.classList.add("user-message");

  } else {
    messageDiv.classList.add("bot-message");
  }

  messageDiv.innerHTML = `
    <img src="../static/public/boy-studing.png" class="user-icon"><p>${message}</p>
    `;

  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}
function sendMessage() {
  const message = messageInput.value.trim();

  if (message !== "") {
    addMessage(message, true);

    fetch("/request", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ prompt: message })
    })
      .then(response => response.json())
      .then(data => {
                  messageInput.value = "";
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("mt-3", "p-3", "rounded");
        messageDiv.classList.add("bot-message");

        const content = data.answer;

        // Check if the content has code block
        const hasCodeBlock = content.includes("```");
        if (hasCodeBlock) {
          // If the content has code block, wrap it in a <pre><code> element
          const codeContent = content.replace(/```([\s\S]+?)```/g, '</p><pre><code>$1</code></pre><p>');


          messageDiv.innerHTML = `<img src="../static/public/logo.png" class="bot-icon"><p>${codeContent}</p>`

        }
        else{
          messageDiv.innerHTML = `<img src="../static/public/logo.png" class="bot-icon"><p>${content}</p>`
        }
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;

      })
      .catch(error => console.error(error));
  }
}


sendBtn.addEventListener("click", function(event) {
  event.preventDefault(); // Prevent the default form submission behavior
  sendMessage();
});

messageInput.addEventListener("keydown", function(event) {
  if (event.keyCode === 13 && !event.shiftKey) {
    event.preventDefault(); // Prevent the default Enter key behavior
    sendMessage();
  }
});
