class Login():
    
    def login_session(auth_data):
        import requests
        session =       requests.session()
        data_account =  session.post('https://test.unnax.com/login', data=auth_data)
        return(session, data_account)
