class GetAccounts:
    
    def __init__(self, account):
        self.account_name =     account['span'][0]['_value']
        self.account_number =   account['p'][0]['_value']
        self.account_currency = account['p'][0]['span'][0]['_value'][0] # TODO create table conversion
        self.account_balance =  account['p'][0]['span'][0]['_value'][1:]
    
    def print_data_account(self):
        print(f"Account data:",                         end="\n         ")
        print(f"Name:       {self.account_name}",       end="\n         ")
        print(f"Number:     {self.account_number}",     end="\n         ")
        print(f"Currency:   {self.account_currency}",   end="\n         ")   
        print(f"Balance:    {self.account_balance}",    end="\n\n    ")