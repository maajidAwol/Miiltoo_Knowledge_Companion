def test_homePage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<title>Dashboard</title>' in response.data
def test_login(client):
    response = client.get('/login')
    assert response.status_code == 200
    assert b'<title>Login Page</title>' in response.data
def test_register(client):
    response = client.get('/signup')
    assert response.status_code == 200

def test_forgetPage(client):
    response = client.get('/forget')
    assert response.status_code == 200
    assert b'<title>Forgot Password</title>' in response.data
