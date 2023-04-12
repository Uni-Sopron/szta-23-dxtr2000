from Player import Player
from Board import Board
from DrawPile import DrawPile
from DiscardPile import DiscardPile

class Game:
    """
    A class representing a game of "Lost Cities".

    Attributes:
        players (list): A list containing instances of the Player class representing the players in the game.
        current_player (Player): The current player whose turn it is to take actions.
        draw_pile (DrawPile): An instance of the DrawPile class representing the draw pile of the game.
        discard_pile (DiscardPile): An instance of the DiscardPile class representing the discard pile of the game.
        board (Board): An instance of the Board class representing the game board.

    Methods:
        __init__(player_names: list): Initializes a new instance of the Game class with the given list of player names,
            creating instances of the Player, DrawPile, DiscardPile, and Board classes.

        play_game(): Runs the game loop until the game is over.

        game_over(): Determines whether the game is over.

        play_turn(): Handles the logic for a single turn of the game.

        advance_to_next_player(): Advances the current player to the next player in the players list.

        display_game_state(): Prints out the current state of the game to the console.

        display_results(): Prints out the final results of the game to the console.
    """
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
