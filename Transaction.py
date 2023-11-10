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
        

    
    def search_transaction(self, search_date):
        filtered_by_date = list(filter(lambda x: x['date'] == search_date, self.transactions_list))
        return filtered_by_date

    def edit_transaction(self, edit_transac):
        self.transactions_list = list(map(lambda x: edit_transac if x['id'] == edit_transac['id'] else x, self.transactions_list))
        

    def get_transactions(self):
        return self.transactions_list
    
    

    def serialize_transactions(self):
        with open("data.json", "w") as write_file:
            json.dump(self.transactions_list, write_file, indent=4, sort_keys=True)
        



with open("data.json", "r") as read_file:
    existing_data = json.load(read_file)


transaction_instance = Transaction(id=1, amount=15, date="2023-01-02", description="Sim Card")


transaction_instance.transactions_list = existing_data


print("All Transactions before Editing:")
print(transaction_instance.get_transactions())


edit_transaction_id = 2
updated_transaction_data = {
    'id': edit_transaction_id,
    'amount': 50,
    'date': '2023-01-05',
    'description': 'Updated Groceries'
}


transaction_instance.edit_transaction(updated_transaction_data)

print("\nAll Transactions after Editing:")
print(transaction_instance.get_transactions())