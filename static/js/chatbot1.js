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

    fetch("/requestH", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt: message }),
    })
      .then((response) => response.json())
      .then((data) => {
        messageInput.value = "";
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("mt-3", "p-3", "rounded");
        messageDiv.classList.add("bot-message");
        sendBtn.style.visibility = "visible";

        const content = data.answer;

        // Check if the content has code block
        const hasCodeBlock = content.includes("```");
        if (hasCodeBlock) {
          // If the content has code block, wrap it in a <pre><code> element
          const codeContent = content.replace(
            /```([\s\S]+?)```/g,
            "</p><pre><code>$1</code></pre><p>"
          );

          messageDiv.innerHTML = `<img src="../static/public/logo.svg" class="bot-icon"><p>${codeContent}</p>`;
        } else {
          messageDiv.innerHTML = `<img src="../static/public/logo.svg" class="bot-icon"><p>${content}</p>`;
        }
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
      })
      .catch((error) => console.error(error));
  }
}

sendBtn.addEventListener("click", function (event) {
  event.preventDefault(); // Prevent the default form submission behavior
  sendMessage();
  sendBtn.style.visibility = "hidden";
  messageInput.value = "";
});

messageInput.addEventListener("keydown", function (event) {
  if (event.keyCode === 13 && !event.shiftKey) {
    event.preventDefault(); // Prevent the default Enter key behavior
    sendMessage();
    sendBtn.style.visibility = "hidden";
    messageInput.value = "";
  }
});
