import html_to_json

class Accounts:
    
    def __init__(self, account):
        account = html_to_json.convert(account.text)
        account = account['html'][0]['body'][0]['div'][0]['div'][0]['ul'][0]['li'][0]
        self.name =     account['span'][0]['_value']
        self.number =   account['p'][0]['_value']
        self.currency = account['p'][0]['span'][0]['_value'][0] # TODO create table conversion
        self.balance =  account['p'][0]['span'][0]['_value'][1:]
    
    def print_data_account(self):
        print("SELF:", self)
        print(f"Account data:",                         end="\n         ")
        print(f"Name:       {self.name}",       end="\n         ")
        print(f"Number:     {self.number}",     end="\n         ")
        print(f"Currency:   {self.currency}",   end="\n         ")   
        print(f"Balance:    {self.balance}",    end="\n\n    ")