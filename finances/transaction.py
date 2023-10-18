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