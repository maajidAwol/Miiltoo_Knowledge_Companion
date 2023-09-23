from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from user import User, db  # Import your User class and db

admin = Admin(name='Admin Panel', template_mode='bootstrap3')

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/my_view.html')

admin.add_view(MyView(name='My View', endpoint='myview'))
admin.add_view(ModelView(User, db.session))
