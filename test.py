import unittest
import os
import json


class loginRegistrationTests(unittest.TestCase):

		#test if login page is loading
		def login(self, username, password):
			return self.app.post('/login', data=dict(username=username,password=password), follow_redirects=True)

		#test if you can log out
		def logout(self):
   			 return self.app.get('/logout', follow_redirects=True)

   		def test_correct_login(self):
			response = self.client.get('/login')
			self.assertIn(b'you are required to login in', response.date)


 # Make the tests executable
if __name__ == "__main__":
    unittest.main()