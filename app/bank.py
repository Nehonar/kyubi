from app.login import Login
from app.get_customers import GetCustomers
from app.get_accounts import GetAccounts

class Bank:
    """ 
        This class manage the structure of data bank
    """

    def __init__(self):
        Login()
        GetAccounts()
        GetCustomers()

    