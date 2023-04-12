from Card import Card

class DrawPile:
    """
    A class representing the draw pile in the game.

    Attributes:
        cards (list): A list containing instances of the Card class representing the cards in the
            draw pile.

    Methods:
        __init__(): Initializes a new instance of the DrawPile class with an empty cards list.
        
        draw_card(): Draws a card from the draw pile and returns it.

    Returns:
        Card: The Card instance that was drawn from the draw pile.
        
    """
    def __init__(self):
        self.cards = []

    def draw_card(self):
        pass