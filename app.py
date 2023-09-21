import time

import PyPDF2
from flask import Flask, redirect, render_template, session, jsonify
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
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename


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
    print(path)
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
    print(path)
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

os.environ["OPENAI_API_KEY"]="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"

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key= "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"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profile.db'  # SQLite database
db = SQLAlchemy(app)


app.config['UPLOAD_FOLDER'] = 'my_books'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def pdf_to_text(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

with app.app_context():
   db.create_all()
    # Add more fields as needed
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            # Username already exists, display an error message
            all_users = User.query.all()

            error_message = "Username already exists. Please choose a different username."
            return render_template('sign_disp.html', users=all_users, error_message=error_message)

        # Create a new user and add it to the database
        new_user = User(full_name=full_name, username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

    # Retrieve all users from the database
    all_users = User.query.all()

    return render_template('sign_disp.html', users=all_users)# You can create an HTML template for the form
@app.route('/auth',methods=['POST','GET'])
def auth():
    allUser = User.query.all()
    username=request.form['username'] 
    password= request.form['password']
    loggedin ='loggedIn'
    for user in allUser:
        if user.username==username:
            if user.password==password:
                return render_template('index.html',loggedin=loggedin )
    return redirect('/login') 
@app.route("/")
def main():
    return render_template("index.html")
# @app.route("/history/")
# def history():
#     book='bk/History student textbook grade 9.pdf'
#     return render_template("book.html",book=book)
# @app.route("/biology/")
# def biology():
#     book = 'bk/Biology Student Textbook Grade 9.pdf'
#     return render_template("book.html",book=book)
@app.route("/grade/")
def grade():
    book = request.args.get('book')
    if book:
       return render_template("book.html",book=book)
    else:
        return render_template("grade.html")
@app.route("/request", methods=["POST"])
def send():
    prompt = request.json.get("prompt")
    book = request.args.get('book')
    choice = request.json.get("book_choice")
    print(choice)
    path = ""

    # if choice == "bk/Biology Student Textbook Grade 9.pdf":
    #     path = "books/Biology Student Textbook Grade 9.txt"
    # elif choice == "bk/History student textbook grade 9.pdf":
    #     path = "books/History student textbook grade 9.txt"
    # else:
    #     print("tired")
    # path = "books/Biology Student Textbook Grade 9.txt"
    url = choice

    # Replace "bk" with "books"
    path = url.replace("bk/", "books/")
    path = path[:-4] + ".txt"
    print(path)

    # result = chat_function(prompt, path)
    # return result
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
@app.route("/quiz_request",methods=["POST"])
def quiz_send():
    quiz_number = request.json.get('number')
    chapter = request.json.get('chapter')
    subtopic = request.json.get('subtopic')
    choice = request.json.get("book_choice")
    prompt = f'generate a {quiz_number} conceptual and random question quiz from  the content specially from {chapter}:characteristics and subtopic {subtopic} having four choices a,b,c,d and answer letter and explanation  of the answer in json format'
    path = ""


    print(choice)

    url = choice

    # Replace "bk" with "books"
    path = url.replace("bk/", "books/")
    path = path[:-4] + ".txt"
    print(path)


    result = quiz_function(prompt, path)
    return result


@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/signup")
def signup():
    return render_template("signup.html")
@app.route("/abcdef")
def abcdef():
    return render_template("custom_book.html")
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return 'No file part'
#
#     file = request.files['file']
#
#     if file.filename == '':
#         return 'No selected file'
#
#     if file and file.filename.endswith('.pdf'):
#         # Save the uploaded file to the UPLOAD_FOLDER
#         filename = secure_filename(file.filename)
#         file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(file_path)
#
#         # Convert the PDF to a text file and save it
#         text_filename = os.path.splitext(filename)[0] + '.txt'
#         text_file_path = os.path.join(app.config['UPLOAD_FOLDER'], text_filename)
#
#         # Use PyPDF2 to extract text from the PDF and save it to the text file
#         pdf_text = pdf_to_text(file_path)
#         with open(text_file_path, 'w', encoding='utf-8') as text_file:
#             text_file.write(pdf_text)
#
#         return 'PDF file uploaded and converted to text successfully'
#
#     return 'Error: Please upload a PDF file'
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file and file.filename.endswith('.pdf'):
        # Save the uploaded PDF file to the "bk" folder in the static directory
        filename = secure_filename(file.filename)
        pdf_file_path = os.path.join(app.static_folder, 'bk', filename)
        file.save(pdf_file_path)

        # Convert the PDF to a text file and save it
        text_filename = os.path.splitext(filename)[0] + '.txt'
        text_file_path = os.path.join('books', text_filename)  # Save in "books" folder

        # Use PyPDF2 to extract text from the PDF and save it to the text file
        pdf_text = pdf_to_text(pdf_file_path)
        with open(text_file_path, 'w', encoding='utf-8') as text_file:
            text_file.write(pdf_text)

        # Calculate the relative path from the "bk" folder including the "bk/" prefix
        relative_pdf_path = os.path.relpath(pdf_file_path, os.path.join(app.static_folder, 'bk'))

        # Render the "books.html" template and pass the relative PDF file path
        print(relative_pdf_path)
        bkr = "bk/"+relative_pdf_path
        print(bkr)
        return render_template("book.html", book=bkr)

    return 'Error: Please upload a PDF file'



if __name__ == "__main__":
    app.run(debug=True)