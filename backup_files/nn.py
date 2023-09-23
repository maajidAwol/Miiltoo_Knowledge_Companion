# import requests
#
# # Specify the model name and API key or token
# model_name = "tiiuae/falcon-7b-instruct"  # Replace with the model name you want to access
# api_key = "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"  # Replace with your actual API key or token
#
# # Define the input text for text generation
# input_text = "explain pysics"
#
# # Define the API endpoint URL
# api_url = f"https://api-inference.huggingface.co/models/{model_name}"
#
# # Set up headers with your API key or token
# headers = {
#     "Authorization": f"Bearer {api_key}"  # Use "Bearer" prefix for tokens
# }
#
# # Create a JSON payload with the input text
# payload = {
#     "inputs": input_text,
#     "options": {
#         "max_length": 100,  # Adjust this to control the length of generated text
#         "num_return_sequences": 1  # Number of text sequences to generate
#     }
# }
#
# # Send a POST request to the Hugging Face API
# response = requests.post(api_url, json=payload, headers=headers)
#
# # Check for successful response
# if response.status_code == 200:
#     data = response.json()
#     generated_text = data[0]['generated_text']
#     print(generated_text)
# else:
#     print(f"Error: {response.status_code} - {response.text}")
from transformers import AutoModelForCausalLM, AutoTokenizer
from PyPDF2 import PdfReader  # Change this import line


def create_llm():
    model_name = "tiiuae/falcon-7b-instruct"  # Replace with the LLM model of your choice
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)  # Set trust_remote_code to True
    model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)  # Set trust_remote_code to True
    return tokenizer, model



def generate_response(input_text, tokenizer, model):
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, top_k=50)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_text


def extract_text_from_pdf(pdf_path):
    text = ""
    pdf_reader = PdfReader(open(pdf_path, "rb"))
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text


def main():
    pdf_path = "../my_books/bio.pdf"  # Path to your PDF file
    text_from_pdf = extract_text_from_pdf(pdf_path)
    print("Reading content from PDF...")

    tokenizer, model = create_llm()

    print("Chat with the content of the PDF:")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = generate_response(user_input, tokenizer, model)
        print(f"LLM: {response}")


if __name__ == '__main__':
    main()
