from app.login import Login
from app.get_customers import Customers
from app.get_accounts import Accounts

class Bank:
    """ 
        This class manage the structure of data bank
    """

    def __init__(self, auth_data):
        (session, data_customers) = Login.login_session(auth_data)
        for account in accounts:
            accounts = Accounts(data_customers)
            Accounts.print_data_account(account)
        # Customers.get(session)