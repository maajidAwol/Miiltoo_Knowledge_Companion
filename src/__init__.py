import os
from flask import Flask
from .extensions import db, bcrypt, mail, migrate, admin
from decouple import config
from .routes.main import main
from .routes.users import users
from .routes.api import api
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from .extensions import admin
# Import your User class and db
from .models.book import Books 
from .models.user import User
from .models.contest import Contest 
class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/my_view.html')

admin.add_view(MyView(name='My View', endpoint='myview'))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Books, db.session))
admin.add_view(ModelView(Contest, db.session))

def create_app():
    app= Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///profile.db'
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
    os.environ["OPENAI_API_KEY"] = config('API_KEY')
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
     
    with app.app_context():
        db.create_all()
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(api)
    
    
    
    
    return app