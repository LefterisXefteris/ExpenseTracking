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
    def search_transaction(cls, search_date):
        filtered_by_date = list(filter(lambda x: x['date'] == search_date, cls.transactions_list))
        return filtered_by_date

        
    @classmethod
    def get_transactions(cls):
        return cls.transactions_list
    
    
    @classmethod
    def serialize_transactions(cls):
        with open("data.json", "w") as write_file:
            json.dump(cls.transactions_list, write_file, indent=4)
        

