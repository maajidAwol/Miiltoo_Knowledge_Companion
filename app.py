import time

import PyPDF2
from flask import Flask, redirect, render_template, session, jsonify, flash, url_for
from flask import Flask, render_template, request
import os
import sys
import re
import json
import openai
from flask_migrate import Migrate
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

import user
from chat_quiz import quiz_function, chat_function
from custom_process import pdf_to_text
from user import register_user,db,User,bcrypt, login_auth,migrate,Books,mail
from admin import admin

os.environ["OPENAI_API_KEY"] = "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"

app = Flask(__name__)
app.static_folder = 'static'
app.secret_key= "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"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profile.db'  # SQLite database
# db = SQLAlchemy(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'miltooknowledgecompanion@gmail.com'
app.config['MAIL_PASSWORD'] = 'kyrmubuougusrlfu'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEBUG'] = True
app.config['MAIL_SUPPRESS_SEND'] = False  # To see the email content in the console


db.init_app(app)
migrate.init_app(app, db)
bcrypt.init_app(app)
mail.init_app(app)
app.config['UPLOAD_FOLDER'] = 'my_books'








if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     full_name = db.Column(db.String(120), nullable=False)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     password = db.Column(db.String(80), nullable=False)
#
# with app.app_context():
#    db.create_all()
#     # Add more fields as needed
@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # full_name = request.form['full_name']
        username = request.form['username']
        password = request.form['password']

        # Call the register_user function
        registration_result = register_user(username, password)

        if not registration_result:
            # user = User.query.filter_by(username=session['email_before']).first()
            check_ver = User.query.filter_by(username=username).first()
            print(check_ver.verified)
            if check_ver.verified:
                # Registration failed, username already exists
                error_message = "Username already exists. Please choose a different username."
                all_users = User.query.all()
                return render_template('sign_disp.html', users=all_users, error_message=error_message)
            elif not check_ver.verified:
                session["email_before"] = username
                return render_template("confirm_email.html")
        elif registration_result:
            user_for_confirmation = User.query.filter_by(username=username).first()
            session["email_before"]= username
            return render_template("confirm_email.html")
    # Retrieve all users from the database
    all_users = User.query.all()

    return render_template('index.html', users=all_users)
@app.route('/auth', methods=['POST', 'GET'])
def auth():
    username = request.form['username']
    password = request.form['password']
    print(username)
    print(password)
    if login_auth(username, password):
        loggedin = 'loggedIn'
        return render_template('index.html', loggedin=loggedin)

    return redirect('/login')

@app.route("/")
def main():
    return render_template("index.html")

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


    url = choice

    # Replace "bk" with "books"
    path = url.replace("bk/", "books/")
    path = path[:-4] + ".txt"
    print(path)

    result = chat_function(prompt, path)
    return result
    # time.sleep(10)
    # if "username" not in session:
    #     ref=path
    # else:
    #     ref =session["username"]+path
    # print(ref)
    #
    # if ref not in session:
    #     session[ref] = []
    # chat_history = session[ref]
    # mock_text = "I am your dedicated study companion, here to empower you in your academic journey. My mission is to assist you in comprehending your course materials and ultimately, helping you achieve better grades. With a wealth of knowledge and insightful analysis at my disposal, I'll break down complex concepts into digestible pieces, provide summaries, answer your questions, and offer valuable insights. Whether it's literature, science, history, or any other subject, I'm here to be your study buddy."
    #
    # result = {"answer": mock_text}  # Mocking the result
    #
    # # Append the current conversation turn to the chat history in the session
    # chat_history.append((prompt, result['answer']))
    # session[ref] = chat_history  # Update the chat history in the session
    #
    # query = None
    # print(result)
    # print(session[ref])
    # return jsonify(result)
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
@app.route("/forget")
def forget():
    return render_template("forget.html")
@app.route("/change_password", methods=['POST'])
def change_password():
    email = request.form['email']
    if user.send_password(email):
        return render_template('login.html')
    elif not user.send_password(email):
        return "no user exist by that username"
@app.route("/abcdef")
def abcdef():
    return render_template("custom_book.html")
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


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    # Query the database to get the first user's data

    user = User.query.filter_by(username=session['username']).first()
    if request.method == 'POST':
        # Handle form submission for saving changes
        user.username = request.form['username']
        user.full_name = request.form['full_name']
        user.email = request.form['email']
        user.school_level = request.form['school_level']
        user.age = request.form['age']
        user.school_name = request.form['school_name']
        user.profile_pic = request.form['profile_pic']
        db.session.commit()

        # Redirect back to the profile page after saving changes
        return redirect('/profile')

    if user:
        return render_template('profile.html', user=user)
    else:
        # Handle the case where no user is found in the database
        return "no user found"


@app.route('/add_book', methods=['POST'])
def add_book():
    # book_url = request.form['book_url']
    #
    # # Create a new book entry for the user
    # new_book = Books(user_id=1, book_url=book_url)  # Assuming user_id=1 for the first user
    # db.session.add(new_book)
    # db.session.commit()
    username = session["username"]

    # Retrieve the user from the database using the username
    user = User.query.filter_by(username=username).first()

    if user:
        book_url = request.form['book_url']

        # Create a new book entry for the user
        new_book = Books(user_id=user.id, book_url=book_url)
        db.session.add(new_book)
        db.session.commit()

    # Redirect back to the profile page after adding the book
    return redirect('/profile')
@app.route('/save_changes', methods=['POST'])
def save_profile():
    # Retrieve the first user from the database

    username = session["username"]

    # Retrieve the user from the database using the username
    user = User.query.filter_by(username=username).first()
    if user:
        if request.method == 'POST':
            # Update user's profile information with data from the form
            # user.username = request.form['username']

            user.full_name = request.form['full_name']
            user.email = request.form['email']
            user.school_level = request.form['school_level']
            user.age = request.form['age']
            user.school_name = request.form['school_name']
            user.profile_pic = request.form['profile_pic']
            db.session.commit()
            flash('Profile changes saved successfully', 'success')
        return redirect('/profile')
    else:
        # Handle the case where no user is found in the database
        return render_template('error.html', message='No user found')

@app.route('/logout')
def logout():
    session['logged_in'] = False
    session.pop('username', None)
    return redirect(url_for('main'))
@app.route('/confirm_email', methods=['GET', 'POST'])
def confirm_email():
    if request.method == 'POST':
        entered_code = request.form.get('verification_code')
        user = User.query.filter_by(username=session['email_before']).first()
        print(entered_code)
        print(user.verification_code)
        print(session["email_before"])

        print(entered_code == user.verification_code)
        if user and entered_code == user.verification_code:
            print("kkkkk")
            # Codes match, complete the registration
            user.verified = True
            db.session.commit()
            return render_template('index.html')
        else:
            return render_template('confirm_email.html')

    return render_template('confirm_email.html')
if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    admin.init_app(app)
    app.run(debug=True)