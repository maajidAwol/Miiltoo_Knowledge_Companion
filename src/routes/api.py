import os

from flask import Blueprint,request
from .utils import chat_function,quiz_function
api = Blueprint('api', __name__)

@api.route("/request", methods=["POST"])
def send():
    prompt = request.json.get("prompt")
    book = request.args.get('book')
    choice = request.json.get("book_choice")
    print(choice)


    print(prompt)
    path = ""
    current_directory = os.path.dirname(__file__)

    # Create the absolute path to the file
    file_path = os.path.join(current_directory, "books/ETH/biology_g-9.txt")
    url = choice

    # Replace "bk" with "books"
    path = url.replace("bk/", "books/")
    path = path[:-4] + ".txt"
    print(path)
    #
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

    current_directory = os.path.dirname(__file__)

    # Create the absolute path to the file
    file_path = os.path.join(current_directory, "books/ETH/biology_g-9.txt")
    if path == "books/Biology Student Textbook Grade 9.txt" or path == "books/History Student Textbook Grade 9.txt":
        prompt = f'generate  {quiz_number} conceptual and random question quiz from  the content specially from {chapter} and subtopic {subtopic} having four choices a,b,c,d and answer letter and explanation  of the answer in json format'
    else:
        prompt = f'generate a {quiz_number} conceptual and random question quiz from  the whole content  having four choices a,b,c,d and answer letter and explanation  of the answer in json format'
    result = quiz_function(prompt, file_path)
    
    return result