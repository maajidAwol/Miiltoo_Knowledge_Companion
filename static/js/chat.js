
const chatBox = document.querySelector("#ccc");
const messageInput = document.querySelector("#aaa");
const sendBtn = document.querySelector("#bbb");
var oda = document.getElementById("book_choice");

function addMessage(message, isUserMessage) {
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("mt-3", "p-3", "rounded");

  if (isUserMessage) {
    messageDiv.classList.add("user-message-container");
  } else {
    messageDiv.classList.add("chatbot-message-container");
  }

  messageDiv.innerHTML = `


                  <span class="user-message-icon">
                    <i class="fa-solid fa-user-tie"></i>
                  </span>
                  <div class="user-message-content">
                   ${message}
                  </div>

    `;

  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}
function sendMessage() {
  const message = messageInput.value.trim();
     const book_choice = oda.value.trim();

  if (message !== "") {

    addMessage(message, true);

    fetch("/request", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt: message , book_choice: book_choice}),
    })
      .then((response) => response.json())
      .then((data) => {
        messageInput.value = "";
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("mt-3", "p-3", "rounded");
        messageDiv.classList.add("chatbot-message-container");
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


          messageDiv.innerHTML = `
                  <span class="chatbot-icon">
                    <img src="/static/asset/logo.svg" alt="">

                  </span>
                  <div class="chatbot-content">
                    ${content}  </div>
                </div>
              `;
        } else {

          messageDiv.innerHTML = `
                  <span class="chatbot-icon">
                    <img src="/static/asset/logo.svg" alt="">

                  </span>
                  <div class="chatbot-content">
                    ${content}   </div>

              `;
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

//messageInput.addEventListener("keydown", function (event) {
//alert("hhh");
//  if (event.keyCode === 13 && !event.shiftKey) {
//    event.preventDefault(); // Prevent the default Enter key behavior
//    sendMessage();
//    sendBtn.style.visibility = "hidden";
//    messageInput.value = "";
//  }
//});
