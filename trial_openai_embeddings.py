import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pre-trained model and tokenizer
model_name = "gpt2"  # You can choose a different model
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Define a function to chat with the chatbot
def chat_with_bot():
    print("Chatbot: Hello! I'm your friendly chatbot.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Encode the user's input
        input_ids = tokenizer.encode(user_input, return_tensors="pt")

        # Generate a response
        with torch.no_grad():
            response_ids = model.generate(input_ids, max_length=50, num_return_sequences=1, no_repeat_ngram_size=2)

        # Decode and print the chatbot's response
        response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
        print("Chatbot:", response)

if __name__ == "__main__":
    chat_with_bot()
