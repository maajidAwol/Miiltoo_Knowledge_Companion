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

os.environ["OPENAI_API_KEY"]="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"

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def main():
    return render_template("index.html")
@app.route("/history/")
def history():
    return render_template("hist-g9.html")
@app.route("/biology/")
def biology():
    return render_template("bio-g9.html")
@app.route("/grade/")
def grade():
    return render_template("grade.html")
@app.route("/request", methods=["POST"])
def send():
    prompt = None
    prompt =request.json.get("prompt")
    PERSIST = False
    if PERSIST and os.path.exists("persist"):
        print("Reusing index...\n")
        vectorstore = Chroma(persist_directory="persist", embedding_function=OpenAIEmbeddings())
        index = VectorStoreIndexWrapper(vectorstore=vectorstore)
    else:

        loader = TextLoader("books/biology.txt", encoding="utf-8")  # Use this line if you only need data.txt
        # loader = DirectoryLoader("data/")
        if PERSIST:
            index = VectorstoreIndexCreator(vectorstore_kwargs={"persist_directory": "persist"}).from_loaders([loader])
        else:
            index = VectorstoreIndexCreator().from_loaders([loader])

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(temperature=0),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    chat_history = []

    result = chain({"question": prompt, "chat_history": chat_history})

    chat_history.append((prompt, result['answer']))
    query = None
    print(result)
    return result
@app.route("/requestH", methods=["POST"])
def ChatWHistory():
    prompt =request.json.get("prompt")
    PERSIST = False
    query = None

    loader = TextLoader("books/history.txt", encoding="utf-8")
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
    quiz_number = request.json.get('number')
    chapter = request.json.get('chapter')
    subtopic = request.json.get('subtopic')
    prompt = f'generate a {quiz_number} conceptual and random question quiz from  the content specially from {chapter}:characteristics and subtopic {subtopic} having four choices a,b,c,d and answer letter and explanation  of the answer in json format'
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
    if r== "fail":
        render_template("bio-g9.html")
    else:
        return r

@app.route("/quiz_requestH",methods=["POST"])
def quizH_send():
    quiz_number = request.json.get('number')
    chapter = request.json.get('chapter')
    subtopic = request.json.get('subtopic')
    prompt = f'generate a {quiz_number} conceptual and random question quiz from  the content specially from {chapter}:characteristics and subtopic {subtopic} having four choices a,b,c,d and answer letter and explanation  of the answer in json format'
    PERSIST = False


    loader = TextLoader("books/history.txt", encoding="utf-8")
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
    if r == "fail":
        render_template("hist-g9.html")
    else:
        return r
if __name__ == "__main__":
    app.run(debug=True)