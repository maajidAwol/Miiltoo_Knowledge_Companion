document.addEventListener("DOMContentLoaded", function () {
    const messageInput = document.querySelector("#user-question");
    const sendBtn = document.querySelector("#ask-btn");
    const resultContainer = document.querySelector("#result-container");
alert("hello")
    function addMessage(message, isUserMessage) {
        // Create message elements and add them to resultContainer
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("result-container-item");

        if (isUserMessage) {
            messageDiv.innerHTML = `
                <div class="user-message-container">
                    <span class="user-message-icon">
                        <i class="fa-solid fa-user-tie"></i>
                    </span>
                    <div class="user-message-content">${message}</div>
                </div>`;
        } else {
            messageDiv.innerHTML = `
                <div class="chatbot-message-container">
                    <span class="chatbot-icon">
                        <img src="/static/asset/logo.svg" alt="">
                    </span>
                    <div class="chatbot-content">${message}</div>
                </div>`;
        }

        resultContainer.appendChild(messageDiv);
    }

    function sendMessage() {
        const message = messageInput.value.trim();

        if (message !== "") {
            addMessage(message, true);

            fetch("/request", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ prompt: message }),
            })
                .then((response) => response.json())
                .then((data) => {
                    addMessage(data.answer, false);
                })
                .catch((error) => console.error(error));
        }
    }

    sendBtn.addEventListener("click", function (event) {
        event.preventDefault();
        sendMessage();
        messageInput.value = ""; // Clear the input after sending
    });

    messageInput.addEventListener("keydown", function (event) {
        if (event.keyCode === 13 && !event.shiftKey) {
            event.preventDefault();
            sendMessage();
            messageInput.value = ""; // Clear the input after sending
        }
    });
});
