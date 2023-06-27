class Card:
    """Represents a card in the game.

    Attributes:
        color (str): The color of the card.
        value (int): The value of the card.
    """

    def __init__(self, color: str, value: int):
        """
        Initializes a new instance of the Card class.

        Args:
            color (str): The color of the card.
            value (int): The value of the card.
        """
        self.color = color
        self.value = value

    def __str__(self):
        """
        Returns the string representation of the card.

        Returns:
            str: The string representation of the card, formatted as "{Color} {Value}".
        """
        return f"{self.color.capitalize()} {self.value}"

    def __repr__(self):
        """
        Returns the string representation of the card for debugging purposes.

        Returns:
            str: The string representation of the card, formatted as "{Color} {Value}".
        """
        return f"{self.color} {self.value}"
