import json

class Transaction:

    transactions_list = []
    
    def __init__(self, id, amount, date, description):
        self.id = id
        self.amount = amount
        self.date = date
        self.description = description

    def add_transaction(self):
        transaction_record = {
            'id': self.id,
            'amount': self.amount,
            'date': self.date,
            'description': self.description
        }
        Transaction.transactions_list.append(transaction_record)
        
    def serialize_transactions(self):
        json_file = "data.json"
        with open(json_file, "w") as write_file:
            json.dump(self.transactions_list, write_file, indent=4, sort_keys=True)

            
    def search_transaction(self, search_date):
        filtered_by_date = list(filter(lambda x: x['date'] == search_date, self.transactions_list))
        return filtered_by_date

    def edit_transaction(self, edit_transac):
        self.transactions_list = list(map(lambda x: edit_transac if x['id'] == edit_transac['id'] else x, self.transactions_list))
        

    def get_transactions(self):
        return self.transactions_list
    
    


        



