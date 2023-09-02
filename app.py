from flask import Flask,render_template
from flask import Flask, render_template, request
import os
import sys
import re
import json
import openai
from langchain.chains import ConversationalRetrievalChain, RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
from langchain.llms import OpenAI
from langchain.vectorstores import Chroma
def ext(text):
  json_pattern = r'\{.*\}'

  # Search for the JSON-like pattern in the text
  match = re.search(json_pattern, text, re.DOTALL)

  if match:
    json_string = match.group()  # Get the matched JSON-like string
    try:
      # Parse JSON-like string into a Python dictionary
      json_object = json.loads(json_string)
      print("Extracted JSON-like object:")
      print(json.dumps(json_object, indent=4))
      return json_object
    except json.JSONDecodeError:
      print("Found a JSON-like pattern, but it's not valid JSON.")
  else:
    print("No JSON-like pattern found in the text.")

os.environ["OPENAI_API_KEY"]=""

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def main():
    return render_template("index.html")
@app.route("/history/")
def history():
    return render_template("hist-g9.html")
@app.route("/grade/")
def grade():
    return render_template("grade.html")
@app.route("/request", methods=["POST"])
def send():
    prompt =request.json.get("prompt")
    PERSIST = False
    query = None

    loader = TextLoader("data/dm.txt", encoding="utf-8")
        # loader = DirectoryLoader("data/")
    index = VectorstoreIndexCreator().from_loaders([loader])

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    chat_history = []

    # message = request.json.get("message")
    # query = input("Prompt: ")

    result = chain({"question": prompt, "chat_history": chat_history})
    print(result)

    chat_history.append((query, result['answer']))
    query = None
    return result
@app.route("/quiz_request",methods=["POST"])
def quiz_send():
    prompt = "generate a five random question quiz from  the content having four choices a,b,c,d and answer letter and detail of the answer in json format"
    PERSIST = False


    loader = TextLoader("books/books.txt", encoding="utf-8")
    # loader = DirectoryLoader("data/")
    index = VectorstoreIndexCreator().from_loaders([loader])

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    query = prompt

    result = chain({"question": prompt, "chat_history": ""})
    print(result)
    r = ext(result["answer"])

    query = None
    return r
if __name__ == "__main__":
    app.run(debug=True)
