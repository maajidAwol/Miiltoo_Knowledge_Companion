import os
import pathlib
import requests
from decouple import config
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
from flask import Blueprint, render_template, request, redirect, flash, session, abort
from ..models.user import User
from ..models.book import Books
from ..extensions import db, mail
from flask_mail import Message
from .utils import register_user, login_auth
from flask_login import login_user, logout_user
client_secrets_file = os.path.join(pathlib.Path(
    __file__).parent, "../../clientSecret.json")
flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email",
            "openid"],
    redirect_uri="https://miltoo.onrender.com/callback"
)
GOOGLE_CLIENT_ID = config('GOOGLE_CLIENT_ID')
users = Blueprint('users', __name__)


@users.route("/login")
def login():
    return render_template("login.html")


@users.route("/signup")
def signup():

    return render_template("signup.html")


@users.route("/forget")
def forget():
    return render_template("forget.html")


@users.route("/change_password", methods=['POST'])
def change_password():
    email = request.form['email']
    if users.send_password(email):
        return render_template('login.html')
    elif not users.send_password(email):
        return "no user exist by that username"


@users.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        # full_name = request.form['full_name']
        username = request.form['username']
        password = request.form['password']
        email = request.form["email"]

        user_google = User.query.filter_by(email=email).first()

        if user_google:

            if user_google.password == "google":
                return render_template("signup.html")
        # Call the register_user function
        registration_result = register_user(username, email, password)

        if not registration_result:
            # user = User.query.filter_by(username=session['email_before']).first()
            check_ver = User.query.filter_by(email=email).first()
            print(check_ver.verified)
            if check_ver.verified:

                error_message = "Username already exists. Please choose a different username."
                all_users = User.query.all()
                return redirect("/login")
            elif not check_ver.verified:
                session["email_before"] = email
                return render_template("confirm_email.html")
        elif registration_result:
            user_for_confirmation = User.query.filter_by(
                username=username).first()
            session["email_before"] = email
            return render_template("confirm_email.html")
    # Retrieve all users from the database
    all_users = User.query.all()

    return render_template('index-new.html', users=all_users)


@users.route('/auth', methods=['POST', 'GET'])
def auth():
    email = request.form['email']
    password = request.form['password']
    print(email)
    print(password)
    if login_auth(email, password):
        if email == "ararsaderese6@gmail.com" or email == "maajidawol@gmail.com" or email == "natnaelmeseret5@gmail.com":
            login_user(User.query.filter_by(email=email).first())
        session['logged_in'] = "true"

        return redirect('/')

    return redirect('/login')


@users.route('/account/', methods=['GET', 'POST'])
def profile():
    # Query the database to get the first user's data

    user = User.query.filter_by(email=session["google_email"]).first()
    if request.method == 'POST':
        # Update user's profile information with data from the form

        user.username = request.form['username']
        # user.email = request.form['email']
        user.school_level = request.form['school_level']
        user.age = request.form['age']
        user.school_name = request.form['school_name']
        user.country = request.form['country']
        user.city = request.form['city']
        # Redirect back to the profile page after saving changes
        return redirect('/account')

    if user:
        return render_template('account.html', user=user)
    else:
        # Handle the case where no user is found in the database
        return "no user found"


@users.route('/add_book', methods=['POST'])
def add_book():
    # Retrieve the first user from the database
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


@users.route('/save_changes', methods=['POST'])
def save_profile():
    # Retrieve the first user from the database

    email = session["google_email"]
    print(email)
    # Retrieve the user from the database using the username
    user = User.query.filter_by(email=email).first()
    if user:
        if request.method == 'POST':
            # Update user's profile information with data from the form
            # user.username = request.form['username']
            if 'profile_pic' in request.files:
                file = request.files['profile_pic']
                if file.filename != '':
                    # Save the uploaded file to the "profile_pic" directory inside the "static" folder
                    pic_url = 'static/profile_pic/' + file.filename
                    file.save(pic_url)
                    user.profile_pic = pic_url
            user.username = request.form['username']
            session["google_name"] = user.username
            # user.email = request.form['email']
            user.school_level = request.form['school_level']
            user.age = request.form['age']
            user.school_name = request.form['school_name']
            user.country = request.form['country']
            user.city = request.form['city']
            # user.profile_pic = request.form['profile_pic']
            db.session.commit()
            flash('Profile changes saved successfully', 'success')
        return redirect('/account')
    else:
        # Handle the case where no user is found in the database
        return render_template('error.html', message='No user found')


@users.route('/logout')
def logout():
    logout_user()
    session['logged_in'] = "false"
    session.pop('username', None)
    return redirect('/')


@users.route('/confirm_email', methods=['GET', 'POST'])
def confirm_email():
    if request.method == 'POST':
        entered_code = request.form.get('verification_code')
        user = User.query.filter_by(email=session['email_before']).first()
        print(entered_code)
        print(user.verification_code)
        print(session["email_before"])

        print(entered_code == user.verification_code)
        if user and entered_code == user.verification_code:
            print("kkkkk")
            # Codes match, complete the registration
            user.verified = True
            db.session.commit()
            session['logged_in'] = "true"
            session["google_name"] = user.username
            session["google_email"] = user.email
            if user.email == "ararsaderese6@gmail.com" or user.email == "maajidawol@gmail.com" or user.email == "natnaelmeseret5@gmail.com":
                login_user(user)
            return redirect('/')
        else:
            return render_template('confirm_email.html')

    return render_template('confirm_email.html')


def login_is_required(function):
    def wruserer(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  # Authorization required
        else:
            return function()

    return wruserer


@users.route("/login_with_google")
def login_with_google():
    authorization_url, state = flow.authorization_url()
    session["state"] = state

    return redirect(authorization_url)


@users.route("/callback")
def callback():
    flow.fetch_token(authorization_response=request.url)

    if not session["state"] == request.args["state"]:
        abort(500)  # State does not match!

    credentials = flow.credentials
    request_session = requests.session()
    cached_session = cachecontrol.CacheControl(request_session)
    token_request = google.auth.transport.requests.Request(
        session=cached_session)

    id_info = id_token.verify_oauth2_token(
        id_token=credentials._id_token,
        request=token_request,
        audience=GOOGLE_CLIENT_ID
    )
    user = User.query.filter_by(email=id_info.get("email")).first()

    if user:
        # User exists, implement your logic here
        session["google_name"] = user.username
        session["google_email"] = user.email
    else:
        # User doesn't exist, implement your logic here
        session["google_id"] = id_info.get("sub")
        session["google_name"] = id_info.get("name")
        session["google_email"] = id_info.get("email")
        profile_url = "/static/asset/profile-pic.png"
        new_user = User(username=session["google_name"], email=session["google_email"], password="google",
                        profile_pic=profile_url)
        db.session.add(new_user)
        db.session.commit()
    if session["google_email"] == "ararsaderese6@gmail.com" or session["google_email"] == "maajidawol@gmail.com" or session["google_email"] == "natnaelmeseret5@gmail.com":
        user = User.query.filter_by(email=session["google_email"]).first()
        login_user(user)
    return redirect("/protected_area")


@users.route("/protected_area")
@login_is_required
def protected_area():
    session['logged_in'] = "true"
    return redirect("/")


@users.route("/booklist")
def booklist():
    books = Books.query.filter_by(user_email=session['google_email'])
    if books:
        return render_template('booklist.html', books=books)
    return render_template('booklist.html')


@users.route("/delete_book")
def delete_book():
    book_name = request.args.get('book_name')
    txt_name = request.args.get('txt_name')
    book = Books.query.filter_by(
        user_email=session['google_email'], book_url=book_name).first()
    db.session.delete(book)
    db.session.commit()
    file_path = os.path.join(users.root_path, book_name)
    os.remove(file_path)
    txt_path = os.path.abspath('src/static/'+txt_name)
    os.remove(txt_path)

    return redirect("/booklist")


@users.route("/contact_us/", methods=['GET', 'POST'])
def contact_us():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = Message(
        'New message from {} <{}>'.format(name, email),
        sender='miltooknowledgecompanion@gmail.com',  # Use your email
        recipients=['ararsaderese6@gmail.com']
    )
    msg.body = message
    mail.send(msg)
    flash('Message sent!', 'success')
    return redirect("/#contact")
