from Expedition import Expedition
from Card import Card

class Board:
    def __init__(self):
        self.expeditions = [Expedition(color) for color in ['yellow', 'green', 'blue', 'white', 'red']]
    
    def add_card(self, card: Card):
        color = card.color.lower()  # kisbetűsre alakítjuk a színt
        print(f"Adding card {color} {card.value}")
        print(f"Index returned by get_expedition: {self.get_expedition(color)}")
        self.expeditions[self.get_expedition(color)].add_card(card)

    def get_expedition(self, color: str):
        colors = ['yellow', 'green', 'blue', 'white', 'red']
        if color not in colors:
            raise ValueError("Invalid color")
        return colors.index(color)  # itt is kisbetűsre alakítjuk a színt
    def __str__(self):
        return '\n'.join([str(expedition) for expedition in self.expeditions])
