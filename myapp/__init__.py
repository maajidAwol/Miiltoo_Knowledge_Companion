import os
from flask import Flask
from .extensions import db, bcrypt, mail, migrate, admin
from decouple import config
from .routes.main import main
from .routes.user import user
from .routes.api import api

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
    app.register_blueprint(user)
    app.register_blueprint(api)
    
    
    
    
    return app