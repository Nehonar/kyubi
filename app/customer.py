class Customer:

    def __init__(self, **args):
        self._qty =              args.get('qty', '')
        self._name =             args.get('name', '')
        self._participation =    args.get('participation', '')
        self._doc =              args.get('doc', '')
        self._address =          args.get('address', '')
        self._emails =           args.get('emails', '')
        self._phones =           args.get('phones', '')
    
    def __str__(self):
        return f'{self.name}'

    @property
    def qty(self):
        return self._qty
    
    @qty.setter
    def qty(self, qty):
        self._qty = qty
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    @property
    def participation(self):
        return self._participation
    
    @participation.setter
    def participation(self, participation):
        self._participation = participation

    @property
    def doc(self):
        return self._doc
    
    @doc.setter
    def doc(self, doc):
        self._doc = doc
    
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, address):
        self._address = address
    
    @property
    def emails(self):
        return self._emails
    
    @emails.setter
    def emails(self, emails):
        self._emails = emails
    
    @property
    def phones(self):
        return self._phones
    
    @phones.setter
    def phones(self, phones):
        self._phones = phones