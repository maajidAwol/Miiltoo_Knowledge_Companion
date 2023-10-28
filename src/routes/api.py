import json
import os
from ..extensions import db
from flask import Blueprint,request
from .utils import chat_function,quiz_function
api = Blueprint('api', __name__)
from .utils import ext
from ..models.contest import Contest
@api.route("/request", methods=["POST"])
def send():
    prompt = request.json.get("prompt")
    book = request.args.get('book')
    choice = request.json.get("book_choice")
    print(choice)


    print(prompt)
    path = ""

    url = choice

    # Replace "bk" with "books"
    path = url.replace("bk/", "books/")
    path = path[:-4] + ".txt"
    print(path)
    path=path[1:]
    file_path = os.path.join(os.path.dirname(__file__), path)
    result = chat_function(prompt, file_path)
    return result
@api.route("/quiz_request", methods=["POST"])
def quiz_send():
    quiz_number = request.json.get('number')
    chapter = request.json.get('chapter')
    subtopic = request.json.get('subtopic')
    choice = request.json.get("book_choice")
    print(quiz_number)
    print(chapter)
    print(subtopic)
    path = ""

    print(choice)

    url = choice

    # Replace "bk" with "books"
    path = url.replace("bk/", "books/")
    path = path[:-4] + ".txt"
    print(path)
    path = path[1:]
    file_path = os.path.join(os.path.dirname(__file__), path)

    if path == "books/ETH/biology_g-9.txt" or path == "books/ETH/history_g-9.txt":
        prompt = f'generate  {quiz_number} conceptual and random question quiz from  the content specially from {chapter} and subtopic {subtopic} having four choices a,b,c,d and answer letter and explanation  of the answer in json format'
    else:
        prompt = f'generate a {quiz_number} conceptual and random question quiz from  the whole content  having four choices a,b,c,d and answer letter and explanation  of the answer in json format'
    result = quiz_function(prompt, file_path)

    return result
@api.route("/contest_generate", methods=["POST"])
def contest_generate():
    prompt = f'generate 1 conceptual and random question quiz from  the content of the book  having four choices a,b,c,d and answer letter and explanation  of the answer in json format'
    files =["books/ETH/biology_g-9.txt","books/ETH/history_g-9.txt","books/ETH/biology_g-9.txt","books/ETH/history_g-9.txt"]
    result = {}
    subject = ["biology","history","chemistry","geography"]
    i=0
    for file in files:
        file_path = os.path.join(os.path.dirname(__file__), file)
        content =  quiz_function(prompt, file_path)

        result.update({subject[i]: content})

        print(i)
        i+=1
    return_result = json.dumps(result)
    sample_contest = Contest(
    subject="grade9",
    contest_data=return_result,
    is_approved=True,
    active=True
        )

    db.session.add(sample_contest)
    db.session.commit()
    return result
