class GetStatements():

    def __init__(self, session, account):
        print("Get statements")
        session.get('http://test.unnax.com/' + account)#+ account['a'][0]['_attributes']['href'])