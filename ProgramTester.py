import unittest
from ExpenseTracking import Transaction

class TestTransactionMethods(unittest.TestCase):

    def test_add_transaction_valid(self):
        # Assuming Transaction class has a method to add and retrieve transactions
        transaction = Transaction()
        transaction.add_transaction('2023-01-01', 100, 'Groceries', 'Bought vegetables')
        self.assertIn('Bought vegetables', transaction.get_transactions())

    def test_serialize_transaction(self):
        # Assuming Transaction class has a serialize method
        transaction = Transaction('2023-01-01', 100, 'Groceries', 'Bought vegetables')
        serialized_data = transaction.serialize_transaction()
        self.assertEqual(serialized_data, {'date': '2023-01-01', 'amount': 100, 'category': 'Groceries', 'description': 'Bought vegetables'})

"""class TestExpenseMethods(unittest.TestCase):

    def test_validate_expense_valid(self):
        # Assuming Expense class has a validate method
        expense = Expense('2023-01-01', 50, 'Groceries', 'Bought vegetables')
        self.assertTrue(expense.validate_expense())

    def test_validate_expense_invalid(self):
        # Assuming Expense class has a validate method
        expense = Expense('2023-01-01', -10, 'Groceries', 'Error')
        self.assertFalse(expense.validate_expense())

class TestIncomeMethods(unittest.TestCase):

    def test_validate_income_valid(self):
        # Assuming Income class has a validate method
        income = Income('2023-01-01', 1000, 'Salary', 'Monthly salary')
        self.assertTrue(income.validate_income())

    def test_validate_income_invalid(self):
        # Assuming Income class has a validate method
        income = Income('2023-01-01', 0, 'Salary', 'Error')
        self.assertFalse(income.validate_income())

class TestCategoryMethods(unittest.TestCase):

    def test_add_to_category(self):
        # Assuming Category class can add transactions and calculate totals
        category = Category('Groceries')
        category.add_to_category(Transaction('2023-01-01', 100, 'Groceries', 'Bought vegetables'))
        self.assertEqual(category.calculate_total(), 100)

    def test_calculate_total_empty(self):
        # Assuming Category class can calculate totals
        category = Category('Utilities')
        self.assertEqual(category.calculate_total(), 0)

class TestGoalMethods(unittest.TestCase):

    def test_contribute_to_goal(self):
        # Assuming Goal class can add contributions and check progress
        goal = Goal('Vacation', 1000)
        goal.contribute_to_goal(100)
        self.assertEqual(goal.check_progress(), 10)

    def test_check_progress_no_contribution(self):
        # Assuming Goal class can check progress
        goal = Goal('New Car', 20000)
        self.assertEqual(goal.check_progress(), 0)

# To run the tests
if __name__ == '__main__':
    unittest.main()
"""