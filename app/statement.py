class Statement:

    def __init__(self, **args):
        self._qty =      args.get('qty', '')
        self._date =     args.get('date', '')
        self._amount =   args.get('amount', '')
        self._balance =  args.get('balance', '')
        self._concept =  args.get('concept', '')

    def __str__(self):
        return f'{self.name}'

    @property
    def qty(self):
        return self._qty
    
    @qty.setter
    def qty(self, qty):
        self._qty = qty

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        self._date = date

    @property
    def amount(self):
        return self._amount
    
    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, balance):
        self._balance = balance

    @property
    def concept(self):
        return self._concept
    
    @concept.setter
    def concept(self, concept):
        self._concept = concept