from Transaction import Transaction
import json


if __name__ == "__main__":

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

    updated_transaction_data.serialize_transactions()


    transaction_instance.edit_transaction(updated_transaction_data)

    print("\nAll Transactions after Editing:")
    print(transaction_instance.get_transactions())

