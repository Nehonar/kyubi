import argparse
from app.login import Login
from app.bank import Bank

parser = argparse.ArgumentParser(description='Login through username and password')
parser.add_argument('--username', required=True, help='Username')
parser.add_argument('--password', required=True, help='Password')
args = parser.parse_args()

auth_data = {
    'username': args.username, 
    'password': args.password
}

(session, html_accounts) = Bank.login(auth_data)

accounts = Bank.get_accounts(html_accounts, session)
customers = Bank.get_customers(session)

print(f"Accounts ( {len(accounts)} )", end="\n\n     ")
for account in accounts:
    # Account data
    print("Account data:",                  end="\n         ")
    print("Name: ",     account.name,       end="\n         ")
    print("Number: ",   account.number,     end="\n         ")
    print("Currency: ", account.currency,   end="\n         ")
    print("Balance: ",  account.balance,    end="\n\n     ")
    # Total customers
    for customer in customers:
        print("Total customers: ", customer.qty,            end="\n         ")
        print("Customer data:",                             end="\n              ")
        print("Name: ", customer.name,                      end="\n              ")
        print("Participation: ", customer.participation,    end="\n              ")
        print("Doc: ", customer.doc,                        end="\n\n              ")
        print("Address", customer.address,                  end="\n\n              ")
        print("Email: ", customer.emails,                    end="\n              ")
        print("Phones: ", customer.phones,                  end="\n\n     ")


# print(GetStatements(session, "statements/1"))



# account_json = html_to_json.convert(account.text)
# account_json = account_json['html'][0]['body'][0]['div'][0]['div'][0]['ul'][0]['li']

# print(f"Accounts ( {len(account_json)} )", end="\n     ")

# for account in account_json:
#     resp_customers = session.get('https://test.unnax.com/customer')
#     resp_statement = session.get('http://test.unnax.com/' + account['a'][0]['_attributes']['href'])
#     statement_json = html_to_json.convert(resp_statement.text)
#     resp_customers = html_to_json.convert(resp_customers.text)
#     data_customers = resp_customers['html'][0]['body'][0]['div'][0]['div'][0]['ul']
#     structuring(resp_customers, statement_json, data_customers, account)