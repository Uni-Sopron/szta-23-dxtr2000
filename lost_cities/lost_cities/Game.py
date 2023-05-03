from Player import Player
from Board import Board
from DrawPile import DrawPile
from DiscardPile import DiscardPile
from Card import Card
import random
import os

class Game:
    def __init__(self, player_names: list):
        self.players = [Player(name) for name in player_names]
        self.current_player = self.players[0]
        self.draw_pile = DrawPile()
        self.discard_pile = DiscardPile()
        self.board = Board()
        self.game_over = False
        self.current_round = 1

        # Shuffle and deal initial hand
        self.draw_pile.shuffle()
        for i, player in enumerate(self.players):
            for _ in range(8):
                player.hand_cards.append(self.draw_pile.cards.pop())

    def play_game(self):
        while not self.game_over:
            self.play_turn()
            if self.current_player == self.players[0]:
                self.current_round += 1
        self.display_results()

    def play_turn(self):
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
        if action == 'play':
            self.play_card()
        elif action == 'discard':
            self.discard_card()
        self.advance_to_next_player()

    def choose_draw_pile(self):
        while True:
            choice = input("Enter 'draw' to draw from the draw pile or 'discard' to draw from the discard pile: ")
            if choice.lower() in ['draw', 'discard']:
                if choice.lower() == 'draw':
                    return self.draw_pile
                else:
                    return self.discard_pile

    def get_player_action(self):
        while True:
            action = input("Enter 'play' to play a card or 'discard' to discard a card: ")
            if action.lower() in ['play', 'discard']:
                return action.lower()

    def play_card(self):
        while True:
            try:
                card_index = int(input("Enter the index of the card you want to play: "))
                self.current_player.play_card(card_index, self.current_player.board)
                break
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

    def discard_card(self):
        while True:
            try:
                card_index = int(input("Enter the index of the card you want to discard: "))
                card = self.current_player.hand_cards[card_index - 1]
                
                for expedition in self.current_player.board.expeditions:
                    if expedition.color == card.color:
                        self.current_player.discard_card(card_index, expedition.discard_pile)
                        print(f"Discarded {card} to {expedition.color.capitalize()} expedition discard pile.")
                        break
                break
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")

    def advance_to_next_player(self):
        current_player_index = self.players.index(self.current_player)
        if current_player_index == len(self.players) - 1:
            self.current_player = self.players[0]
        else:
            self.current_player = self.players[current_player_index + 1]

    def display_game_state(self):
        os.system("CLS")
        print(f"\nRound {self.current_round}")
        print(f"Current player: {self.current_player.name}")
        print(f"{self.current_player.name}'s hand: {[str(card) for card in self.current_player.hand_cards]}")
        print(f"Draw pile: {len(self.draw_pile.cards)} cards")
        for expedition in self.current_player.board.expeditions:
            if expedition.started:
                print(f"{expedition.color.capitalize()} expedition started with cards: {[str(card) for card in expedition.cards]} Discard pile: {[str(card) for card in expedition.discard_pile.cards]}")
            else:
                print(f"{expedition.color.capitalize()} expedition not started | Discard pile: {[str(card) for card in expedition.discard_pile.cards]}")
        print("\n")

    def display_results(self):
        print("Game over!")
        print("Game results:")
        for expedition in self.current_player.board.expeditions:
            if expedition.cards:
                print(f"{expedition.color.capitalize()} expedition: {expedition.get_points()} points")
            else:
                print(f"{expedition.color.capitalize()} expedition: Not started")
        for player in self.players:
            print(f"{player.name}: {player.points} points")