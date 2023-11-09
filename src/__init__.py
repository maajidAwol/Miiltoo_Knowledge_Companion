import os
from flask import Flask
from .extensions import db, bcrypt, mail, migrate, admin, login
from decouple import config
from .routes.main import main
from .routes.users import users
from .routes.utils import save_first_contest
from .routes.api import api
from .routes.error_handlers import errors
from flask import redirect, url_for
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from .models.book import Books 
from .models.user import User
from .models.contest import Contest
from .models.user_contest import UserContest
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
class MyView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated
    @expose('/')
    def index(self):
        return self.render('admin/my_view.html')
class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated
    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        
        return redirect(url_for('main.index'))

admin.add_view(MyView(name='Generate Contest', endpoint='myview'))
admin.add_view(MyModelView(User, db.session))
admin.add_view(MyModelView(Books, db.session))
admin.add_view(MyModelView(Contest, db.session))
admin.add_view(MyModelView(UserContest, db.session))

def create_app(database_uri='sqlite:///profile.db'):
    app= Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = config('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = config('MAIL_PASSWORD')
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_DEBUG'] = True
    app.config['MAIL_SUPPRESS_SEND'] = False
    app.static_folder = 'static'
    app.secret_key = config('SECRET_KEY')
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    mail.init_app(app)
    admin.init_app(app)
    login.init_app(app)
    os.environ["OPENAI_API_KEY"] = config('API_KEY')
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
     
    with app.app_context():
        db.create_all()
        save_first_contest()
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(api)
    app.register_blueprint(errors)
    
    return app
