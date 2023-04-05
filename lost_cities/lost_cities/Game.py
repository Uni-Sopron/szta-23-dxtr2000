from Player import Player
from Board import Board
from DrawPile import DrawPile
from DiscardPile import DiscardPile

class Game:
    def __init__(self, player_names: list):
        self.players = [Player(name) for name in player_names]
        self.current_player = self.players[0]
        self.draw_pile = DrawPile()
        self.discard_pile = DiscardPile()
        self.board = Board()

    def play_game(self):
        pass
        
    def game_over(self):
        pass        
    def play_turn(self):
        pass  
    def advance_to_next_player(self):
        pass    
    def display_game_state(self):
        pass      
    def display_results(self):
        pass
