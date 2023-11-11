import json
import re
from flask import session
import random
import string
import PyPDF2
from flask_mail import Message
from ..extensions import db, bcrypt, mail
from ..models.user import User
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from datetime import datetime, timedelta
from ..models.contest import Contest
from .topics import biology, history,rt,cont_hist,cont_geo,cont_chem,sudan_hist
def generate_verification_code():
    first_digit = random.choice(string.digits[1:])  # Choose a digit from 1 to 9
    rest_of_digits = ''.join(random.choice(string.digits) for _ in range(3))
    return first_digit + rest_of_digits
def generate_random_password():
    first_digit = random.choice(string.digits[1:])  # Choose a digit from 1 to 9
    rest_of_digits = ''.join(random.choice(string.digits) for _ in range(5))
    return first_digit + rest_of_digits
def register_user(username, email ,password):
    # Check if the username already exists
    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        # Username already exists, return False to indicate registration failure
        return False

    # Generate a 4-digit verification code
    verification_code = generate_verification_code()

    # Hash the password before storing it
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    # Create a new user and add it to the database
    send_verification_email(email, verification_code)
    profile_url ="/static/asset/profile-pic.png"
    new_user = User(username=username,email=email, password=hashed_password, verification_code = verification_code,profile_pic=profile_url)
    db.session.add(new_user)
    db.session.commit()

    # Send the verification code to the user's email


    # Return True to indicate successful registration
    return True

def send_verification_email(email, verification_code):
    msg = Message('Email Confirmation Code', sender='your_email@gmail.com', recipients=[email])
    msg.body = f'Your verification code is: {verification_code}'
    mail.send(msg)
def send_(email, verification_code):
    msg = Message('Email Confirmation Code', sender='your_email@gmail.com', recipients=[email])
    msg.body = f'Your verification code is: {verification_code}'
    mail.send(msg)

def login_auth(email, password):
    user = User.query.filter_by(email=email).first()

    if user and bcrypt.check_password_hash(user.password, password) and user.verified:
        # Password is correct, allow login
        session['logged_in'] = True
        session["google_name"] = user.username
        session["google_email"] = email

        return True

    # Password is incorrect
    return False
def send_password(email):
    existing_user = User.query.filter_by(username=email).first()

    if existing_user and existing_user.verified:
        # Username already exists, return False to indicate registration failure
        print()
        password = generate_random_password()
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        existing_user.password = hashed_password
        db.session.commit()
        print("after"+existing_user.password)
        msg = Message('Email Confirmation Code', sender='miltooknowledgecompanion@gmail.com', recipients=[email])
        msg.body = f'Your new password is: {password}'
        mail.send(msg)
        return True
    else:
        return False
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

    print(path+"jjj")
    index = VectorstoreIndexCreator().from_loaders([loader])

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )
    # session.pop("hist", None)
    # if "bio" not in session:
    #     session["bio"] = []
    if path not in session:
        session[path] = []

    # chat_history = session["bio"]
    chat_history = session[path]
    result = chain({"question": prompt, "chat_history": chat_history})

    # Append the current conversation turn to the chat history in the session
    chat_history.append((prompt, result['answer']))
    # session[path] = chat_history
    # print(session[path])
    # session["bio"] = chat_history  # Update the chat history in the session
    session[path] = chat_history

    query = None
    print(result)
    # print(session["bio"])
    print(session[path])
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

    return r
def pdf_to_text(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
def replace_space(filename):
    for i in range(len(filename)):
        if filename[i]==' ':
            filename[i]='_'
    return filename
def save_first_contest():
    r = ext(rt)
    hist_cont =ext(cont_hist)
    geo_cont =ext(cont_geo)
    chem_cont =ext(cont_chem)
    subject = "biology"
    dict_contest = {subject: r}

    dict_contest.update({"history": hist_cont})
    dict_contest.update({"chemistry": chem_cont})
    dict_contest.update({"geography": geo_cont})
    str_contest = json.dumps(dict_contest)
    # result = ext(r)
    # return result
    # db.session.query(Contest).delete()
    # db.session.commit()
    random_suffix = ''.join(random.choice(string.ascii_letters) for _ in range(6))

    # Generate a random contest ID by concatenating "grade9" with the current time and the random suffix
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    contest_id = f'grade9_{current_time}_{random_suffix}'
    
    


    # Create the Contest instance with the generated ID
    sample_contest = Contest(
        contest_id=contest_id,
        contest_data=str_contest,
        is_approved=True,
        start_time=datetime.now(),
        end_time=datetime.now() + timedelta(days=100),
        
    )
    exist= Contest.query.filter_by(title="Mock Contest").first()
    if not exist:
        db.session.add(sample_contest)
        db.session.commit()