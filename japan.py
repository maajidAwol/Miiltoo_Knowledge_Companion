# import openai
#
# # Set your OpenAI API key here
# api_key = "YOUR_API_KEY"
#
# # Initialize the OpenAI API client
# openai.api_key = api_key
#
# # Define a function to chat with the chatbot
# def chat_with_bot():
#     print("Chatbot: Hello! I'm your friendly chatbot.")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == 'exit':
#             print("Chatbot: Goodbye!")
#             break
#
#         # Generate a response from GPT-3
#         response = openai.Completion.create(
#             engine="text-davinci-002",  # You can choose a different engine
#             prompt=user_input,
#             max_tokens=50,  # Adjust the max tokens as needed
#             n = 1  # Number of responses to generate
#         )
#
#         # Extract and print the chatbot's response
#         chatbot_response = response.choices[0].text
#         print("Chatbot:", chatbot_response)
#
# if __name__ == "__main__":
#     chat_with_bot()
import openai
from transformers import AutoTokenizer, AutoModelForCausalLM

# Set your OpenAI API key here
api_key = "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"

# Initialize the OpenAI API client
openai.api_key = api_key

# Initialize the Hugging Face tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("gpt2")  # You can choose a different model
model = AutoModelForCausalLM.from_pretrained("gpt2")

# Define a function to embed text and chat with the chatbot
def chat_with_bot():
    print("Chatbot: Hello! I'm your friendly chatbot.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Embed user input using Hugging Face's model
        input_ids = tokenizer.encode(user_input, return_tensors="pt")
        with open("output.txt", "w", encoding="utf-8") as file:
            file.write(tokenizer.decode(input_ids[0]))

        # Generate a response from GPT-3
        with open("output.txt", "r", encoding="utf-8") as file:
            input_text = file.read()
            response = openai.Completion.create(
                engine="text-davinci-002",  # You can choose a different engine
                prompt=input_text,
                max_tokens=50,  # Adjust the max tokens as needed
                n=1  # Number of responses to generate
            )

            # Extract and print the chatbot's response
            chatbot_response = response.choices[0].text
            print("Chatbot:", chatbot_response)

if __name__ == "__main__":
    chat_with_bot()
