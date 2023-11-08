import Transaction

class Expense(Transaction):

    def __init__(self, amount, date, description, category, payment_method):
        super().__init__(self, amount, date, description)
        self.category = category
        self.payment_method = payment_method


    def is_deductible(self):
        pass

    def apply_discount(self, discount):
        pass
