import json
import os
from flask import Blueprint, app, render_template, request
from ..models.contest import Contest
from .topics import biology, history,rt,cont_hist
from .utils import ext, pdf_to_text
from ..extensions import db
from werkzeug.utils import secure_filename
main = Blueprint('main', __name__)

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

        sample_contest = Contest(
            subject="grade9",
            contest_data=contest_data,
            is_approved=True,
            active=True
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

@main.route("/contest/")
def contest():
    return render_template("contest.html")
@main.route('/upload', methods=['POST'])
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
        bkr = "bk/" + relative_pdf_path
        print(bkr)

        json_data = {

        }
        return render_template("book-new.html", book=bkr, json_data=json_data, )

    return 'Error: Please upload a PDF file'
@main.route("/contest_request", methods=["POST"])
def contest_send():
    r = ext(rt)
    hist_cont =ext(cont_hist)

    subject = "biology"
    dict_contest = {subject: r}

    dict_contest.update({"history": hist_cont})
    dict_contest.update({"chemistry": r})
    dict_contest.update({"geography": r})
    str_contest = json.dumps(dict_contest)
    # result = ext(r)
    # return result
    # db.session.query(Contest).delete()
    # db.session.commit()
    print(r)
    print(dict_contest)
    sample_contest = Contest(
        subject="grade9",
        contest_data=str_contest,
        is_approved=True,
        active=True
    )

    db.session.add(sample_contest)
    db.session.commit()
    contest_query = Contest.query.first()
    result = ext(contest_query.contest_data)
    print(result)
    return result