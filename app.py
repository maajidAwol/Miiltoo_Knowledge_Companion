import time

from flask import Flask, render_template, session, jsonify
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
def chat_function(prompt,path):
    loader = TextLoader(path, encoding="utf-8")  # Use this line if you only need data.txt

    index = VectorstoreIndexCreator().from_loaders([loader])

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )
    # session.pop("hist", None)
    if "bio" not in session:
        session["bio"] = []

    chat_history = session["bio"]
    result = chain({"question": prompt, "chat_history": chat_history})

    # Append the current conversation turn to the chat history in the session
    chat_history.append((prompt, result['answer']))
    session["bio"] = chat_history  # Update the chat history in the session

    query = None
    print(result)
    print(session["bio"])
    return result
def quiz_function(prompt, path):

    loader = TextLoader(path, encoding="utf-8")
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

os.environ["OPENAI_API_KEY"]=""

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key= "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"
@app.route("/")
def main():
    return render_template("index.html")
@app.route("/history/")
def history():
    book='bk/History student textbook grade 9.pdf'
    return render_template("book.html",book=book)
@app.route("/biology/")
def biology():
    book = 'bk/Biology Student Textbook Grade 9.pdf'
    return render_template("book.html",book=book)
@app.route("/grade/")
def grade():
    return render_template("grade.html")
@app.route("/request", methods=["POST"])
def send():
    prompt = request.json.get("prompt")
    choice = request.json.get("book_choice")
    print(choice)
    path = ""
    if choice == "bk/Biology Student Textbook Grade 9.pdf":
        path = "books/biology.txt"
    elif choice == "bk/History student textbook grade 9.pdf":
        path = "books/history.txt"
    # path = "books/biology.txt"
    # result = chat_function(prompt, path)
    time.sleep(10)
    if "bio" not in session:
        session["bio"] = []
    chat_history = session["bio"]
    mock_text = "I am your dedicated study companion, here to empower you in your academic journey. My mission is to assist you in comprehending your course materials and ultimately, helping you achieve better grades. With a wealth of knowledge and insightful analysis at my disposal, I'll break down complex concepts into digestible pieces, provide summaries, answer your questions, and offer valuable insights. Whether it's literature, science, history, or any other subject, I'm here to be your study buddy."

    result = {"answer": mock_text}  # Mocking the result

    # Append the current conversation turn to the chat history in the session
    chat_history.append((prompt, result['answer']))
    session["bio"] = chat_history  # Update the chat history in the session

    query = None
    print(result)
    print(session["bio"])
    return jsonify(result)

# @app.route("/requestH", methods=["POST"])
# def ChatWHistory():
#     # prompt = request.json.get("prompt")
#     # path = "books/history.txt"
#     # result = chat_function(prompt, path)
#     time.sleep(10)
#     chat_history = session["bio"]
#     mock_text = "I am your dedicated study companion, here to empower you in your academic journey. My mission is to assist you in comprehending your course materials and ultimately, helping you achieve better grades. With a wealth of knowledge and insightful analysis at my disposal, I'll break down complex concepts into digestible pieces, provide summaries, answer your questions, and offer valuable insights. Whether it's literature, science, history, or any other subject, I'm here to be your study buddy."
#
#     result = {"answer": mock_text}  # Mocking the result
#
#     # Append the current conversation turn to the chat history in the session
#     chat_history.append(("kk", result['answer']))
#     session["bio"] = chat_history  # Update the chat history in the session
#
#     query = None
#     print(result)
#     print(session["bio"])
#     return jsonify(result)
@app.route("/quiz_request",methods=["POST"])
def quiz_send():
    quiz_number = request.json.get('number')
    chapter = request.json.get('chapter')
    subtopic = request.json.get('subtopic')
    choice = request.json.get("book_choice")
    prompt = f'generate a {quiz_number} conceptual and random question quiz from  the content specially from {chapter}:characteristics and subtopic {subtopic} having four choices a,b,c,d and answer letter and explanation  of the answer in json format'
    path = ""


    print(choice)
    path = ""
    if choice == "bk/Biology Student Textbook Grade 9.pdf":
        path = "books/biology.txt"
    elif choice == "bk/History student textbook grade 9.pdf":
        path = "books/history.txt"
    result = quiz_function(prompt, path)
    return result


# @app.route("/quiz_requestH",methods=["POST"])
# def quizH_send():
#     quiz_number = request.json.get('number')
#     chapter = request.json.get('chapter')
#     subtopic = request.json.get('subtopic')
#     prompt = f'generate a {quiz_number} conceptual and random question quiz from  the content specially from {chapter}:characteristics and subtopic {subtopic} having four choices a,b,c,d and answer letter and explanation  of the answer in json format'
#     path = "books/history.txt"
#     result = quiz_function(prompt, path)

    return result
if __name__ == "__main__":
    app.run(debug=True)