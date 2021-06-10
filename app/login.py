import requests

class Login:

    def login_session(self):

        session =       requests.session()
        data_account =  session.post('https://test.unnax.com/login', data=self)
        print(session)
        if data_account.status_code == 200:
            print("Login OK")
            return(session, data_account.text)
        else:
            print("Error login")
            # TODO create table to status code
            return(session, data_account.text)

    def login_customers(self):
        data_customer = self.get('https://test.unnax.com/customer')
        if data_customer.status_code == 200:
            print("Customers OK")
            return data_customer.text
        else:
            print("Error customers")
            return data_customer.text
