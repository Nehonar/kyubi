class Account:
    def __init__(self, **args):
        self._name =         args.get('name', '')
        self._number =       args.get('number', '')
        self._currency =     args.get('currency', '')
        self._balance =      args.get('balance', '')
        self._customers =    args.get('customers', '')
        self._statements =   args.get('statements', '')
    
    def __str__(self):
        return f'{self.name}'

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, number):
        self._number = number

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        self._currency = currency

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def customers(self):
        return self._customers

    @customers.setter
    def customers(self, customers):
        self._customers = customers

    @property
    def statements(self):
        return self._statements

    @statements.setter
    def statements(self, statements):
        self._statements = statements