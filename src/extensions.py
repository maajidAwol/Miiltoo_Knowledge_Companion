from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from flask_migrate import Migrate
from flask_admin import Admin
from flask_login import LoginManager
bcrypt = Bcrypt()
mail = Mail()
migrate = Migrate()
db = SQLAlchemy()
admin=Admin(name='Admin Panel', template_mode='bootstrap3')
login=LoginManager()
