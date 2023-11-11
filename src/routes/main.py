import json
import os
from flask import Blueprint, app, render_template, request, session, flash
from ..models.contest import Contest
from ..models.user import User
from ..models.book import Books
from ..models.user_contest import UserContest
from .topics import biology, history,rt,cont_hist,cont_geo,cont_chem,sudan_hist
from .utils import ext, pdf_to_text,replace_space
from ..extensions import db
from datetime import datetime
import random
import string
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, BooleanField
from datetime import datetime, timedelta


main = Blueprint('main', __name__)
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class RegistrationForm(FlaskForm):
    registered = BooleanField('Registered')
    submit = SubmitField('Update Registration')
@main.route('/')
def index():
    return render_template('index-new.html')
@main.route("/grade/")
def grade():
    book = request.args.get('book')

    if book:
        if book == "bk/ETH/biology_g-9.pdf":
            json_data = biology
            print(biology)
            print(book)
            return render_template("book-new.html", book=book, json_data=json_data)
        elif book == "bk/ETH/history_g-9.pdf":
            json_data = history
            print(history)
            return render_template("book-new.html", book=book, json_data=json_data)
        elif book == "bk/SS/history_g-9.pdf":
            json_data = sudan_hist
            print(sudan_hist)
            return render_template("book-new.html", book=book, json_data=json_data)
        else:

            json_data = {
                "None": {
                    "none": [],
                }
            }
            return render_template("book-new.html", book=book)

    else:

        return render_template("grade.html")
from flask import jsonify

@main.route("/save_contest_data", methods=["POST"])
def save_contest_data():
    if request.method == 'POST':
        data = request.get_json()  # Assuming data is sent as JSON
        contest_data = data.get('contestData', '')  # Extract 'contestData' from the JSON
        random_suffix = ''.join(random.choice(string.ascii_letters) for _ in range(6))
        current_time = datetime.now().strftime('%Y%m%d%H%M%S')
        contest_id = f'grade9_{current_time}_{random_suffix}'
        print(contest_id)
        sample_contest = Contest(
            contest_id = contest_id,
            contest_data=contest_data,
            is_approved=True,

        )

        db.session.add(sample_contest)
        db.session.commit()

        # Return a JSON response
        response_data = {
            "message": "Contest data saved successfully",
            "contestData": contest_data
        }

        return jsonify(response_data)
    else:
        # Handle invalid requests or other HTTP methods
        return "Method not allowed", 405  # Return a 405 Method Not Allowed status


# @main.route('/contest/', methods=['GET', 'POST'])
# def contest():
#     if request.method == 'POST':
#         # Handle the registration logic here
#         user_email = session.get('google_email')
#         contest_id = session.get('contest_id')
#
#         if user_email and contest_id:
#             user = User.query.filter_by(email=user_email).first()
#
#             if user:
#                 user_contest = UserContest.query.filter_by(user_email=user_email, contest_id=contest_id).first()
#
#                 if user_contest:
#                     user_contest.registered = True
#                     db.session.commit()
#                 else:
#                     new_user_contest = UserContest(
#                         user_email=user_email,
#                         contest_id=contest_id,
#                         registered=True
#                     )
#                     db.session.add(new_user_contest)
#                     db.session.commit()
#                 return jsonify({'success': True, 'message': 'Registration successful'})
#             else:
#                 return jsonify({'success': False, 'message': 'User not found'})
#         else:
#             return jsonify({'success': False, 'message': 'User email or contest ID not found in the session'})
#
#     return render_template('contest.html')

#
@main.route('/contest/', methods=['GET', 'POST'])
def contest():
    if request.method == 'POST':
        # Handle the registration logic here
        user_email = session.get('google_email')
        contest_query = Contest.query.filter(Contest.is_approved.is_(True)).first()
        session["contest_id"] = contest_query.contest_id
        contest_id = session.get('contest_id')




        if user_email and contest_id:
            user = User.query.filter_by(email=user_email).first()

            if user:
                user_contest = UserContest.query.filter_by(user_email=user_email, contest_id=contest_id).first()

                if user_contest:
                    user_contest.registered = True
                    db.session.commit()
                else:
                    new_user_contest = UserContest(
                        user_email=user_email,
                        contest_id=contest_id,
                        registered=True
                    )
                    db.session.add(new_user_contest)
                    db.session.commit()
                return jsonify({'success': True, 'message': 'Registration successful'})
            else:
                return jsonify({'success': False, 'message': 'User not found'})
        else:
            return jsonify({'success': False, 'message': 'User email or contest ID not found in the session'})
    contest_query = Contest.query.filter(Contest.is_approved.is_(True)).first()
    if "logged_in" not in session or not session["logged_in"]:
        return redirect("/login")
    if contest_query:
        session['contest_id'] =contest_query.contest_id
    # Calculate the contest start and end times
    if not contest_query:
        return redirect("/leaderboard")
    now = datetime.now().strftime('%Y%m%d%H%M%S')
    contest_start_time = contest_query.start_time
    contest_end_time = contest_query.end_time


    contest_id = session['contest_id']
    user_email = session['google_email']
    user_contest_entry = UserContest.query.filter_by(user_email=user_email, contest_id=contest_id).first()
    contest= Contest.query.all()
    # if user_contest_entry and user_contest_entry.finished_contest:
    #     return redirect("/leaderboard")

    return render_template('contest.html', contest=contest)

@main.route('/finish_contest/', methods=['POST'])
def finish_contest():
    print(session['contest_id'])
    print(session['google_email'])

    contest_id = session['contest_id']
    user_email = session['google_email']

    biology_score = request.json.get('biology')
    history_score = request.json.get('history')
    chemistry_score = request.json.get('chemistry')
    geography_score = request.json.get('geography')

    user_contest_entry = UserContest.query.filter_by(user_email = user_email, contest_id=contest_id).first()

    if user_contest_entry:
        # Update the subject scores and total
        user_contest_entry.biology = biology_score
        user_contest_entry.history = history_score
        user_contest_entry.chemistry = chemistry_score
        user_contest_entry.geography = geography_score
        user_contest_entry.finished_contest = True
        user_contest_entry.total = sum(
            [score for score in [biology_score, history_score, chemistry_score, geography_score] if score is not None])
        db.session.commit()

    response = {'success': True, 'message': 'Contest data updated successfully'}
    return jsonify(response)
# @main.route("/register_for_contest/")
# def register_for_contest():
#     pass
@main.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file and allowed_file(file.filename):
        # Save the uploaded PDF file to the "static/bk" folder
        filename = secure_filename(file.filename)
        
        filename=replace_space(filename)
        pdf_file_path = os.path.join(os.path.dirname(__file__), '../static/bk', filename)
        file.save(pdf_file_path)
        
        # Convert the PDF to a text file and save it in the "routes/books" folder
        text_filename = os.path.splitext(filename)[0] + '.txt'
        text_filename=replace_space(text_filename)
        text_file_path = os.path.join(os.path.dirname(__file__), 'books', text_filename)

        # Use pdfminer.six to extract text from the PDF and save it to the text file
        pdf_text = pdf_to_text(pdf_file_path)
        with open(text_file_path, 'w', encoding='utf-8') as text_file:
            text_file.write(pdf_text)

        # Calculate the relative path for rendering the template
        relative_pdf_path = os.path.relpath(pdf_file_path, os.path.join(os.path.dirname(__file__), '../static/bk'))
        bkr = "bk/" + relative_pdf_path
        book=Books(user_email=session['google_email'],book_name=file.filename,book_url='books/'+text_filename,txt_url= 'bk/'+filename)
        exist=Books.query.filter_by(user_email=session['google_email'],book_url='books/'+text_filename).first()
        if not exist:
            db.session.add(book)
            db.session.commit()
        json_data = {}  # You can define the json_data here

        return render_template("book-new.html", book=bkr, json_data=json_data)

    return 'Error: Please upload a PDF file'







@main.route("/contest_request", methods=['GET', 'POST' ])
def contest_send():
    current_time = datetime.now().strftime('%Y%m%d%H%M%S')
    contest_query = Contest.query.filter(Contest.is_approved.is_(True)).first()
    session["contest_id"] = contest_query.contest_id

    current_time = datetime.strptime(current_time, '%Y%m%d%H%M%S')

    if not contest_query.start_time:
        return redirect("/leaderboard")
    if contest_query.start_time <= current_time <= contest_query.end_time:
        result = ext(contest_query.contest_data)
        print(current_time)
        # contest_query.is_approved =False
        # db.session.commit()
        return result
    else:
        return redirect("/leaderboard")
@main.route("/leaderboard")
def leaderboard():
    contest_id_from_session = session.get('contest_id')

    if contest_id_from_session:
        leaderboard_data = UserContest.query.filter_by(contest_id=contest_id_from_session).order_by(
            UserContest.total.desc()).all()

        return render_template("leaderboard.html", leaderboard_data=leaderboard_data)
    else:
        return "Contest ID not found in the session."
@main.route('/get_chat_history', methods=['POST'])
def get_chat_history():
    choice = request.json.get("book_choice")
    path = ""

    url = choice

    # Replace "bk" with "books"
    path = url.replace("bk/", "books/")
    path = path[:-4] + ".txt"
    print(path)
    path=path[1:]
    file_path = os.path.join(os.path.dirname(__file__), path)
    chat_history = session.get(file_path, [])
    print(path)
    return jsonify(chat_history)

