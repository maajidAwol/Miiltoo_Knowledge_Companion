import json
import os
from flask import Blueprint, app, render_template, request
from ..models.contest import Contest
from .topics import biology, history,rt,cont_hist,cont_geo,cont_chem
from .utils import ext, pdf_to_text
from ..extensions import db
from werkzeug.utils import secure_filename
main = Blueprint('main', __name__)
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


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

    if file and allowed_file(file.filename):
        # Save the uploaded PDF file to the "static/bk" folder
        filename = secure_filename(file.filename)
        pdf_file_path = os.path.join(os.path.dirname(__file__), '../static/bk', filename)
        file.save(pdf_file_path)

        # Convert the PDF to a text file and save it in the "routes/books" folder
        text_filename = os.path.splitext(filename)[0] + '.txt'
        text_file_path = os.path.join(os.path.dirname(__file__), 'books', text_filename)

        # Use pdfminer.six to extract text from the PDF and save it to the text file
        pdf_text = pdf_to_text(pdf_file_path)
        with open(text_file_path, 'w', encoding='utf-8') as text_file:
            text_file.write(pdf_text)

        # Calculate the relative path for rendering the template
        relative_pdf_path = os.path.relpath(pdf_file_path, os.path.join(os.path.dirname(__file__), '../static/bk'))
        bkr = "bk/" + relative_pdf_path

        json_data = {}  # You can define the json_data here

        return render_template("book-new.html", book=bkr, json_data=json_data)

    return 'Error: Please upload a PDF file'

@main.route("/contest_request", methods=["POST"])
def contest_send():
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