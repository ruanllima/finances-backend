from datetime import datetime
from . import settings

class Transaction:
    def __init__(self, amount: float, category: int, description: str = "") -> None:
        """Initialize a object Transaction.

        Args:
            amount (float): transaction value
            category (int): transaction category
            description (str): transaction description. Defaults to "".
        """
        self.amount = amount
        self.category = category 
        self.description = description
        self.date = datetime.now()
        
    def __str__(self) -> str:
        """Generates a transaction string.

        Returns:
            str: transaction description
        """
        return f"""
        =====================================
        Transação: {self.description}
        R$ {self.amount:.2f} 
        ({settings.CAT_STRING[self.category]})
        ====================================="""
        
    def update(self, **attributes) -> None:
        for attr in attributes:
            setattr(self, attr, attributes[attr])