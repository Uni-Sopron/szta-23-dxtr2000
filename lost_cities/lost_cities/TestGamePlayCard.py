import unittest
from unittest.mock import patch, Mock
from Game import Game
from Player import Player


class GamePlayCardTestCase(unittest.TestCase):
    @patch('builtins.input', side_effect=['42', '1'])
    def test_play_card(self, mock_input):
        game = Game(['Player 1', 'Player 2'])
        player_mock = Mock(spec=Player)
        game.current_player = player_mock

        game.play_card()

        player_mock.play_card.assert_called_with(1, game.current_player.board)


if __name__ == '__main__':
    unittest.main()
