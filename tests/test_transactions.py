from finances import Transaction

DEFAULT_AMOUNT = 100.00
DEFAULT_CATEGORY = 1
DEFAULT_DESCRIPTION = "Test transaction"

def get_transaction() -> Transaction:
    """Generates a transaction test.

    Returns:
        _type_: Test transaction
    """
    return Transaction(DEFAULT_AMOUNT, DEFAULT_CATEGORY, DEFAULT_DESCRIPTION)

def test_transactions_instance():
    """Checks if the objects instantiate correctly."""
    tr = get_transaction()
    assert isinstance(tr, Transaction)

def test_transactions_attributes():
    """Check the values and types."""
    tr = get_transaction()
    
    # Check the values.
    assert tr.amount == DEFAULT_AMOUNT, "The value of transaction is INCORRECT!"
    assert tr.category == DEFAULT_CATEGORY, "The value of category is INCORRECT!"
    assert tr.description == DEFAULT_DESCRIPTION, "The value of description is INCORRECT!"
    # Check the types.
    assert type(tr.amount) is float, "The value of transaction not is FLOAT!"
    assert type(tr.category) is int, "The value of category not is INT!"
    assert type(tr.description) is str, "The value of description not is STR!"
    
def test_update_attributes():
    
 