class Card:
    """
    A class representing a card in the game.

    Attributes:
        color (str): The color of the card, represented as a string.
        value (int): The value of the card, represented as an integer.

    Methods:
        __init__(color: str, value: int): Initializes a new instance of the Card class with the given color
            and value.

    Parameters:
        color (str): The color of the card. Must be one of the following: "yellow", "green", "blue",
            "white", or "red".
        value (int): The value of the card. Must be a positive integer.
    """
    def __init__(self, color: str, value: int):
        self.color = color
        self.value = value