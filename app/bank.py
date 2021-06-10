import logging
import requests

from requests.sessions import session

from app import Status
from app.customer import Customer
from app.account import Account
from app.statement import Statement
from bs4 import BeautifulSoup

log = logging.getLogger('Bank')

class Bank:
    """ 
        This class manage the structure of data bank
    """
    _html_accounts = None
    _session = None
    _url = "https://test.unnax.com/"

    def __init__(self):
        self._session = requests.session()

    def login(self, auth_data):
        log.info('Start login')
        response =  self._session.post(self._url + 'login', data=auth_data)

        if "Login" in response.text or not response.ok:
            log.error("Failed login")
            return Status.LoginError

        self._html_accounts = response.text
        log.info("Login OK")
        return Status.LoginOk

    def get_accounts(self):
        html_accounts = BeautifulSoup(self._html_accounts, 'html.parser')
        list_accounts = html_accounts.find_all('li', {'class': 'collection-item'})
        
        accounts = []

        for data_account in list_accounts:
            account = Account()

            account.name =      data_account.span.string
            account.number =    data_account.find('p').getText()[0:20]
            account.currency =  data_account.p.span.string[0] # TODO create table conversion
            account.balance =   data_account.p.span.string[1:]
            # In case to crush statement or customer pass to next account
            try:
                account.statements = self._get_statements(data_account.find_all('a')[0]['href'])
                account.customers = self._get_customers()
            except Exception as e:
                log.error(e)
                continue

            accounts.append(account)

        return accounts
    
    def _get_customers(self):
        resp = self._session.get(self._url + 'customer')

        if not resp.ok:
            log.error("Error customers")
            raise Exception("Error, no existen customers")
        
        log.info("Get customers")

        html_customers = BeautifulSoup(resp.text, 'html.parser')
        list_customers = html_customers.find_all('ul', {'class': 'collection'})
        
        customers = []

        for data_customer in list_customers:
            customer = Customer()

            customer.qty =  len(list_customers)
            customer.name = data_customer.find_all('li', {'class': 'collection-header'})[0].string
            # Data items
            data_item =         data_customer.find_all('li', {'class': 'collection-item'})
            customer.address =  data_item[2].string
            customer.emails =   data_item[1].string
            customer.phones =   data_item[0].string
            # Special items
            # TODO this info none exist in customer
            customer.doc = None
            customer.participation = "Titular"
            
            customers.append(customer)
        
        return customers

    def _get_statements(self, link_statement):
        resp = self._session.get(self._url + link_statement)
        html_statements = BeautifulSoup(resp.text, 'html.parser')
        list_statements = html_statements.find_all('tr')
        
        statements = []

        for data_statement in list_statements:
            statement = Statement()

            statement.qty = len(data_statement)
            statements.append(statement)
        
        return statements
