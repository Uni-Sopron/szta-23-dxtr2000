from Expedition import Expedition


class Board:
    """
    A class representing the game board for the game "The Lost Expedition".

    Attributes:
        expeditions (list): A list containing instances of the Expedition class, representing the
            five expeditions in the game (yellow, green, blue, white, and red).

    Methods:
        __init__(): Initializes a new instance of the Board class with empty expeditions. Creates
            Expedition instances for each color and appends them to the expeditions list.
    """

    def __init__(self):
        self.expeditions = []
        for color in ['yellow', 'green', 'blue', 'white', 'red']:
            self.expeditions.append(Expedition(color))
