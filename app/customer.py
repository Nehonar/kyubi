class Customer:

    def __init__(self, **args):
        self.qty =              args.get('qty', '')
        self.name =             args.get('name', '')
        self.participation =    args.get('participation', '')
        self.doc =              args.get('doc', '')
        self.address =          args.get('address', '')
        self.emails =           args.get('emails', '')
        self.phones =           args.get('phones', '')
    
    def __str__(self):
        return f'{self.name}'

    # TODO poner como accounts