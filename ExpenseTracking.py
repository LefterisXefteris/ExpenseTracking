import json


class Transaction:

    transactions_list = []
    
    def __init__(self, amount, date, description):
        self.amount = amount
        self.date = date
        self.description = description

    def add_transaction(self):
        transaction_record = {
            'amount': self.amount,
            'date': self.date,
            'description': self.description
        }
        Transaction.transactions_list.append(transaction_record)
        
        
    @classmethod
    def get_transactions(cls):
        return cls.transactions_list
    
    
    @classmethod
    def serialize_transactions(cls):
        with open("data.json", "w") as write_file:
            json.dump(cls.transactions_list, write_file, indent=4)
        



transaction1 = Transaction(100, '2023-01-01', 'Groceries')
transaction1.add_transaction()
Transaction.serialize_transactions() 