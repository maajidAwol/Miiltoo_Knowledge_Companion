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
os.environ["OPENAI_API_KEY"]=""

app = Flask(__name__)
@app.route("/")
def main():
    return render_template("index.html")
@app.route("/history/")
def history():
    return render_template("hist-g9.html")

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
if __name__ == "__main__":
    app.run(debug=True)
