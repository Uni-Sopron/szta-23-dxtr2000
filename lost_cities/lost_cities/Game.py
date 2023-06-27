import os

from Board import Board
from DiscardPile import DiscardPile
from DrawPile import DrawPile
from Player import Player


class Game:
    """Represents a game of the card game.

    Attributes:
        players (list): The list of players participating in the game.
        current_player (Player): The current player taking their turn.
        draw_pile (DrawPile): The draw pile of the game.
        discard_pile (DiscardPile): The shared discard pile of the game.
        board (Board): The game board containing the expeditions.
        game_over (bool): Indicates if the game is over.
        current_round (int): The current round number.
    """

    def __init__(self, player_names: list):
        """
        Initializes a new instance of the Game class.

        Args:
            player_names (list): The list of player names.
        """
        self.players = [Player(name) for name in player_names]
        self.current_player = self.players[0]
        self.draw_pile = DrawPile()
        self.discard_pile = DiscardPile()
        self.board = Board()
        self.game_over = False
        self.current_round = 1

        self.draw_pile.shuffle()
        for i, player in enumerate(self.players):
            for _ in range(8):
                player.hand_cards.append(self.draw_pile.cards.pop())

    def play_game(self):
        """
        Plays the game until it is over.
        """
        while not self.game_over:
            self.play_turn()
            if self.current_player == self.players[0]:
                self.current_round += 1
        self.display_results()

    def play_turn(self):
        """
        Plays a single turn of the current player.
        """
        self.display_game_state()
        if not self.discard_pile.cards:
            draw_pile = self.draw_pile
            print("Discard pile is empty. Drawing from draw pile.")
        elif self.current_player == self.players[0]:
            draw_pile = self.draw_pile
            print("First round. Drawing from draw pile.")
        elif not self.draw_pile.cards:
            print("Draw pile is empty. Game over.")
            self.game_over = True
            return
        else:
            draw_pile = self.choose_draw_pile()
        self.current_player.draw_card(draw_pile)
        action = self.get_player_action()
        if action == "play":
            self.play_card()
        elif action == "discard":
            self.discard_card()
        self.advance_to_next_player()

    def choose_draw_pile(self):
        """
        Allows the current player to choose the draw pile.

        Returns:
            DrawPile or DiscardPile: The chosen draw pile.
        """
        while True:
            choice = input(
                "Enter 'draw' to draw from the draw pile or 'discard' to draw from the discard pile: "
            )
            if choice.lower() in ["draw", "discard"]:
                if choice.lower() == "draw":
                    return self.draw_pile
                else:
                    return self.discard_pile

    def get_player_action(self):
        """
        Allows the current player to choose an action.

        Returns:
            str: The chosen action ('play' or 'discard').
        """
        while True:
            action = input(
                "Enter 'play' to play a card or 'discard' to discard a card: "
            )
            if action.lower() in ["play", "discard"]:
                return action.lower()

    def play_card(self):
        """
        Plays a card from the current player's hand.
        """
        while True:
            try:
                card_index = int(input("Enter the index of the card you want to play: "))
                self.current_player.play_card(card_index, self.current_player.board)
                break
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

    def discard_card(self):
        """
        Discards a card from the current player's hand.
        """
        while True:
            try:
                card_index = int(
                    input("Enter the index of the card you want to discard: ")
                )
                card = self.current_player.hand_cards[card_index - 1]

                for expedition in self.current_player.board.expeditions:
                    if expedition.color == card.color:
                        self.current_player.discard_card(
                            card_index, expedition.discard_pile
                        )
                        print(
                            f"Discarded {card} to {expedition.color.capitalize()} expedition discard pile."
                        )
                        break
                break
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

    def advance_to_next_player(self):
        """
        Advances the turn to the next player.
        """
        current_player_index = self.players.index(self.current_player)
        if current_player_index == len(self.players) - 1:
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[current_player_index + 1]

    def display_game_state(self):
        """
        Displays the current state of the game.
        """
        os.system("CLS")
        print(f"\nRound {self.current_round}")
        print(f"Current player: {self.current_player.name}")
        print(
            f"{self.current_player.name}'s hand: {[str(card) for card in self.current_player.hand_cards]}"
        )
        print(f"Draw pile: {len(self.draw_pile.cards)} cards")
        for expedition in self.current_player.board.expeditions:
            if expedition.started:
                print(
                    f"{expedition.color.capitalize()} expedition started with cards: {[str(card) for card in expedition.cards]} Discard pile: {[str(card) for card in expedition.discard_pile.cards]}"
                )
            else:
                print(
                    f"{expedition.color.capitalize()} expedition not started | Discard pile: {[str(card) for card in expedition.discard_pile.cards]}"
                )
        print("\n")

    def display_results(self):
        """
        Displays the final results of the game.
        """
        print("Game over!")
        print("Game results:")
        for expedition in self.current_player.board.expeditions:
            if expedition.cards:
                print(
                    f"{expedition.color.capitalize()} expedition: {expedition.get_points()} points"
                )
            else:
                print(f"{expedition.color.capitalize()} expedition: Not started")
        for player in self.players:
            print(f"{player.name}: {player.points} points")
