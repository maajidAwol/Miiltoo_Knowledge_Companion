# from langchain import HuggingFacePipeline
# from transformers import AutoTokenizer, pipeline
# import torch
#
# model = "tiiuae/falcon-7b-instruct" #tiiuae/falcon-40b-instruct
#
# tokenizer = AutoTokenizer.from_pretrained(model)
#
# pipeline = pipeline(
#     "text-generation", #task
#     model=model,
#     tokenizer=tokenizer,
#     torch_dtype=torch.bfloat16,
#     trust_remote_code=True,
#     device_map="auto",
#     max_length=200,
#     do_sample=True,
#     top_k=10,
#     num_return_sequences=1,
#     eos_token_id=tokenizer.eos_token_id
# )
# llm = HuggingFacePipeline(pipeline = pipeline, model_kwargs = {'temperature':0})
# from langchain import PromptTemplate,  LLMChain
#
# template = """
# You are an intelligent chatbot. Help the following question with brilliant answers.
# Question: {question}
# Answer:"""
# prompt = PromptTemplate(template=template, input_variables=["question"])
#
# llm_chain = LLMChain(prompt=prompt, llm=llm)
#
# question = "create 5 question quiz in form of json object make it in json format "
#
# print(llm_chain.run(question))
from langchain.llms import HuggingFaceHub

# Initialize the HuggingFaceHub instance
hf = HuggingFaceHub(repo_id="tiiuae/falcon-7b-instruct", huggingfacehub_api_token="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")

def chat_with_bot():
    print("Chatbot: Hello! How can I assist you today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ("exit", "quit", "bye"):
            print("Chatbot: Goodbye!")
            break

        # Generate a response from the chatbot model
        response = hf(user_input)

        print("Chatbot:", response)


if __name__ == "__main__":
    chat_with_bot()

