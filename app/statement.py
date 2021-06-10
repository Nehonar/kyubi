class Statement:

    def __init__(self, **args):
        self.qty =      args.get('qty', '')
        self.date =     args.get('date', '')
        self.amount =   args.get('amount', '')
        self.balance =  args.get('balance', '')
        self.concept =  args.get('concept', '')

    def __str__(self):
        return f'{self.name}'