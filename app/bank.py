import logging
from app.login import Login
from app.customers import Customer
from app.accounts import Account
from bs4 import BeautifulSoup

class Bank:
    """ 
        This class manage the structure of data bank
    """
    log = logging.getLogger('Bank')

    def login(self):
        # self.log.info('Start login')
        (session, html_accounts) = Login.login_session(self)

        return (session, html_accounts)

    def get_accounts(self,session):
        html_accounts = BeautifulSoup(self, 'html.parser')
        list_accounts = html_accounts.find_all('li', {'class': 'collection-item'})
        
        accounts = []

        for data_account in list_accounts:
            account = Account()

            account.name =      data_account.span.string
            account.number =    data_account.find('p').getText()[0:20]
            account.currency =  data_account.p.span.string[0] # TODO create table conversion
            account.balance =   data_account.p.span.string[1:]
            accounts.append(account)

        return accounts
    
    def get_customers(self):
        resp = Login.login_customers(self)
        html_customers = BeautifulSoup(resp, 'html.parser')
        list_customers = html_customers.find_all('ul', {'class': 'collection'})
        
        customers = []

        for data_customer in list_customers:
            customer = Customer()

            customer.qty =              len(list_customers)
            customer.name =             data_customer.find_all('li', {'class': 'collection-header'})[0].string
            # Data items
            data_item = data_customer.find_all('li', {'class': 'collection-item'})
            customer.address =          data_item[2].string
            customer.emails =           data_item[1].string
            customer.phones =           data_item[0].string
            # Special items
            # TODO search other option to find this info
            if len(data_item) >= 4:
                customer.doc = data_item[3].string
            else:
                customer.doc = "None"

            if len(data_item) >= 5:
                customer.participation = data_item[4].string
            else:
                customer.participation = "Titular"
            
            customers.append(customer)
        
        return customers

    def get_statements(self):
        print(self)
