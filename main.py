from Transaction import Transaction

if __name__ == "__main__":
    first_transaction = Transaction(15, "2023-01-02", "Sim Card")
    first_transaction.add_transaction()
    first_transaction.serialize_transactions()