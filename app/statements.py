class GetStatements:

    def __init__(self, session, account):
        print("Init get statements")
        session.get('http://test.unnax.com/' + account['a'][0]['_attributes']['href'])