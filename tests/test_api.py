import unittest,requests

class TestApi(unittest.TestCase):
    Main_URl="http://127.0.0.1:5000"
    login_URL=Main_URl+"/login"
    register_URL=Main_URl+"/signup"
    
    
    def test_Main_URL_response(self):
        resp=requests.get(self.Main_URl)
        self.assertEqual(resp.status_code,200)
        print("Test 1 passed")
    def test_login_URL_response(self):
        resp=requests.get(self.login_URL)
        self.assertEqual(resp.status_code,200)
        print("Test 2 passed")
    def test_register_URL_response(self):
        resp=requests.get(self.register_URL)
        self.assertEqual(resp.status_code,200)
        print("Test 3 passed")
   
if __name__ == '__main__':
    tester= TestApi()
    tester.test_Main_URL_response()
    tester.test_login_URL_response()
    tester.test_register_URL_response()
        