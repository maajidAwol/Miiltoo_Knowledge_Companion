from flask_admin import BaseView, expose
from flask_admin.contrib.sqla import ModelView
from ..extensions import admin
# Import your User class and db
from ..extensions import db
from ..models.book import Books 
from ..models.user import User
from ..models.contest import Contest 

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/my_view.html')

admin.add_view(MyView(name='My View', endpoint='myview'))
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Books, db.session))
admin.add_view(ModelView(Contest, db.session))
