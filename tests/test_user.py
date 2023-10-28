from src.models.user import User

def test_registration(client,app):
    response=client.post('/register',data={"username":"test","email":"test@gmail.com","password":"test"})
    assert response.status_code == 200
    
    with app.app_context():
        assert User.query.count()==1
        assert User.query.filter_by(username="test").first() is not None
        assert User.query.filter_by(email="test@gmail.com").first() is not None
        
def test_login(client,app):
    client.post('/register',data={"username":"test","email":"test@gmail.com","password":"test"})
    response=client.post('/auth',data={"email":"test@gmail.com","password":"test"})
    assert response.status_code == 302
