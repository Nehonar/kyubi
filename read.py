import argparse
import logging
from os import stat

from app.bank import Bank
from app import Status

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger("read")

if __name__ == "__main__":

    # Get data authentication
    parser = argparse.ArgumentParser(description='Login through username and password')
    parser.add_argument('--username', required=True, help='Username')
    parser.add_argument('--password', required=True, help='Password')
    args = parser.parse_args()
    auth_data = {
        'username': args.username, 
        'password': args.password
    }

    # Bank petitions
    bank = Bank()

    login_status = bank.login(auth_data)
    if login_status == Status.LoginError:
        log.error("Fail in login get out")
        exit(1)

    accounts = bank.get_accounts()

    # Print info accounts
    print(f"Accounts ( {len(accounts)} )")
    for account in accounts:
        # Account data
        print("Account data:",              end="\n         ")
        print("Name: ",     account.name,       end="\n         ")
        print("Number: ",   account.number,     end="\n         ")
        print("Currency: ", account.currency,   end="\n         ")
        print("Balance: ",  account.balance,    end="\n\n     ")
        # Total customers
        for customer in account.customers:
            print("Total customers: ", customer.qty,            end="\n         ")
            print("Customer data:",                             end="\n              ")
            print("Name: ", customer.name,                      end="\n              ")
            print("Participation: ", customer.participation,    end="\n              ")
            print("Doc: ", customer.doc,                        end="\n\n              ")
            print("Address", customer.address,                  end="\n\n              ")
            print("Email: ", customer.emails,                   end="\n              ")
            print("Phones: ", customer.phones,                  end="\n\n     ")
            print(f"Statements ( {len(account.statements)} )",       end="\n              ")
            print("Date           |  Amount  | Balance   | Concept", end="\n\n              ")
        for statement in account.statements:
            print(f"{statement.date}     |    {statement.amount}   |   {statement.balance}   |  {statement.concept}", end="\n\n              ")
        
        