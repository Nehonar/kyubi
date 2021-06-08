import html_to_json

class Customers:

    def get(self, session):
        print("Init get customer")
        # session.get("https://test.unnax.com/customer")

        # data_customers = html_to_json.convert(data_customers.text)
        # qty_curtomers = len(data_customers['html'][0]['body'][0]['div'][0]['div'][0]['ul'])
        # cust_data = data_customers[0]['li']
        # cust_name = data_customers[0]['li'][0]['h4'][0]['_value']
        # cust_participation = data_customers[0]['li']
        # cust_doc = data_customers[0]['li']
        # cust_address = data_customers[0]['li'][3]['_value']
        # cust_emails = data_customers[0]['li'][2]['_value']
        # cust_phones = data_customers[0]['li'][1]['_value']
        # print(f"Total customers: {qty_curtomers}", end="\n          ")
        # print("Customer data:", end="\n             ")
        # print(f"Name: {customer_name}", end="\n             ")
        # if len(customer_data) == 5: # TODO check if there is any way to find out the Titular or Authorized
        #     print(f"Participation: {customer_participation[5]['_value']}", end="\n             ")
        # else:
        #     print(f"Participation: Titular", end="\n             ")

        # if len(customer_data) == 6: # TODO check if there is any way to find out the Doc
        #     print(f"Doc: {customer_doc[6]['_value']}", end="\n             ")
        # else:
        #     print(f"Doc: -", end="\n\n             ")
        # print(f"Address:    {customer_address}", end="\n\n             ")
        # print(f"Emails:     {customer_emails}", end="\n             ")
        # print(f"Phones:     {customer_phones}", end="\n\n     ")