from finances import Transaction

def test_transactions():
    tr = Transaction()
    assert isinstance(tr, Transaction)