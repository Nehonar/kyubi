import unittest
import json

from app.bank import Bank

with open('test/config.json', 'r') as file:
    config = json.load(file)

class TestMethods(unittest.TestCase):

    def test_bank_loguin_ok(self):
        auth_data = {
            'username': config["TESTING_LOGIN"]["USERNAME"],
            'password': config["TESTING_LOGIN"]["PASSWORD"]
        }
        bank = Bank()
        
        self.assertEqual(bank.login(auth_data), 1)

    def test_bank_login_fake_user(self):
        auth_data = {
            'username': config["TESTING_LOGIN"]["DATA_FAKE"],
            'password': config["TESTING_LOGIN"]["PASSWORD"]
        }
        bank = Bank()

        self.assertEqual(bank.login(auth_data), 2)
    
    def test_bank_login_fake_pass(self):
        auth_data = {
            'username': config["TESTING_LOGIN"]["USERNAME"],
            'password': config["TESTING_LOGIN"]["DATA_FAKE"]
        }
        bank = Bank()

        self.assertEqual(bank.login(auth_data), 2)

if __name__ == '__main__':
    unittest.main()