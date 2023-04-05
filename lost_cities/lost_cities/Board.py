from Expedition import Expedition

class Board:
    def __init__(self):
        self.expeditions = []
        for color in ['yellow', 'green', 'blue', 'white', 'red']:
            self.expeditions.append(Expedition(color))