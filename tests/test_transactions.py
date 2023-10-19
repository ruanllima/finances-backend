from finances import Transaction, settings
from datetime import datetime


DEFAULT_AMOUNT = 100.00
DEFAULT_CATEGORY = settings.CAT_EDUCATION
DEFAULT_DESCRIPTION = "Test transaction"
STRING_TESTE = """
        =====================================
        Transação: {self.description}
        R$ {self.amount:.2f} 
        ({settings.CAT_STRING[self.category]})
        ====================================="""

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
    before = datetime.now()
    tr = get_transaction()
    
    # Check the values.
    assert tr.amount == DEFAULT_AMOUNT, "The value of transaction is INCORRECT!"
    assert tr.category == DEFAULT_CATEGORY, "The value of category is INCORRECT!"
    assert tr.description == DEFAULT_DESCRIPTION, "The value of description is INCORRECT!"
    assert tr.date <= datetime.now(), "The date of transaction cannot is future"
    assert tr.date >= before, "The transaction date must be after 'before'"
    
    # Check the types.
    assert type(tr.amount) is float, "The type of transaction not is FLOAT!"
    assert type(tr.category) is int, "The type of category not is INT!"
    assert type(tr.description) is str, "The type of description not is STR!"
    assert type(tr.date) is datetime, "The type of data is incorrect"
    
def test_transactions_print():
    """Check if the transaction is correct"""
    tr = get_transaction()
    assert str(tr) == STRING_TESTE
    
def test_transactions_update():
    """Check attribute updates"""
    tr = get_transaction()
    
    # Check amount update
    tr.update(amount=200.00)
    assert tr.amount == 200.00, "The value has not been update!"
    
    # Check category update
    tr.update(category=settings.CAT_FOOD)
    assert tr.category == settings.CAT_FOOD, "The category has not been update!"
    
    # Check description update
    tr.update(description="Teste")
    assert tr.description == "Teste", "The description has not been update!"
    
    # Check date update
    tr.update(date=datetime(2020, 10, 15))
    assert tr.date == datetime(2020, 10, 15), "The date has not been update!"
    

    