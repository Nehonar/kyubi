import unittest
import json

from app.bank import Bank
from bs4 import BeautifulSoup

with open('test/config.json', 'r') as file:
    config = json.load(file)

username = config["TESTING_LOGIN"]["USERNAME"]
password = config["TESTING_LOGIN"]["PASSWORD"]
data_fake = config["TESTING_LOGIN"]["DATA_FAKE"]

bank = Bank()

class TestMethods(unittest.TestCase):

    # Test login
    def test_bank_loguin_ok(self):
        auth_data = {
            'username': username,
            'password': password
        }
        
        self.assertEqual(bank.login(auth_data), 1)

    def test_bank_login_fake_user(self):
        auth_data = {
            'username': data_fake,
            'password': password
        }

        self.assertEqual(bank.login(auth_data), 2)
    
    def test_bank_login_fake_pass(self):
        auth_data = {
            'username': username,
            'password': data_fake
        }

        self.assertEqual(bank.login(auth_data), 2)

    # Test get_accounts
    def test_get_accounts(self):
        accounts = bank.get_accounts()

        self.assertEqual(accounts[0].name, "Cuenta personal")

    # Test _get_customers
    def test_get_customers(self):
        customers = bank._get_customers()

        self.assertEqual(customers[0].name, "Pepito Perez")

    # Test _get_statements
    def test_get_statements(self):
        statements = bank._get_statements("statements/1")

        self.assertEqual(statements[0].date, "05/07/2018")

if __name__ == '__main__':
    unittest.main()