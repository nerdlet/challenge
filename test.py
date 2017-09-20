
import os
import unittest


 
class loginRegistrationTests(unittest.TestCase):
 
    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
 
    # executed after each test
    def tearDown(self):
        pass
 
    def test_index_page(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
 
if __name__ == "__main__":
    unittest.main()