from bs4 import BeautifulSoup

class Account:
    def __init__(self, **args):
        self.name =         args.get('name', '')
        self.number =       args.get('number', '')
        self.currency =     args.get('currency', '')
        self.balance =      args.get('balance', '')
        self.customers =    args.get('customers', '')
    
    def __str__(self):
        return f'{self.name}'