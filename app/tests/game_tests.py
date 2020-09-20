import unittest
from app.models.game import Game
from app.models.player import Player

class TestGame(unittest.TestCase):

    def test_p1_rock_p2_scissors(self):
        self.player_1 = Player("David", "Rock")
        self.player_2 = Player("Kyle", "Scissors")
        self.game = Game(self.player_1, self.player_2)
        self.game.who_wins(self.player_1, self.player_2)
        self.assertEqual("Player 1 WINS with Rock!", self.game.who_wins(self.player_1, self.player_2))

    def test_p1_rock_p2_paper(self):
        self.player_1 = Player("David", "Rock")
        self.player_2 = Player("Kyle", "Paper")
        self.game = Game(self.player_1, self.player_2)
        self.game.who_wins(self.player_1, self.player_2)
        self.assertEqual("Player 2 WINS with Paper!", self.game.who_wins(self.player_1, self.player_2))

    def test_p1_rock_p2_rock(self):
        self.player_1 = Player("David", "Rock")
        self.player_2 = Player("Kyle", "Rock")
        self.game = Game(self.player_1, self.player_2)
        self.game.who_wins(self.player_1, self.player_2)
        self.assertEqual("It's a DRAW, play again!", self.game.who_wins(self.player_1, self.player_2))

    def test_p1_paper_p2_rock(self):
        self.player_1 = Player("David", "Paper")
        self.player_2 = Player("Kyle", "Rock")
        self.game = Game(self.player_1, self.player_2)
        self.game.who_wins(self.player_1, self.player_2)
        self.assertEqual("Player 1 WINS with Paper!", self.game.who_wins(self.player_1, self.player_2))

    def test_p1_paper_p2_scissors(self):
        self.player_1 = Player("David", "Paper")
        self.player_2 = Player("Kyle", "Scissors")
        self.game = Game(self.player_1, self.player_2)
        self.game.who_wins(self.player_1, self.player_2)
        self.assertEqual("Player 2 WINS with Scissors!", self.game.who_wins(self.player_1, self.player_2))

    def test_p1_paper_p2_paper(self):
        self.player_1 = Player("David", "Paper")
        self.player_2 = Player("Kyle", "Paper")
        self.game = Game(self.player_1, self.player_2)
        self.game.who_wins(self.player_1, self.player_2)
        self.assertEqual("It's a DRAW, play again!", self.game.who_wins(self.player_1, self.player_2))

    def test_p1_scissors_p2_paper(self):
        self.player_1 = Player("David", "Scissors")
        self.player_2 = Player("Kyle", "Paper")
        self.game = Game(self.player_1, self.player_2)
        self.game.who_wins(self.player_1, self.player_2)
        self.assertEqual("Player 1 WINS with Scissors!", self.game.who_wins(self.player_1, self.player_2))

    def test_p1_scissors_p2_rock(self):
        self.player_1 = Player("David", "Scissors")
        self.player_2 = Player("Kyle", "Rock")
        self.game = Game(self.player_1, self.player_2)
        self.game.who_wins(self.player_1, self.player_2)
        self.assertEqual("Player 2 WINS with Rock!", self.game.who_wins(self.player_1, self.player_2))

    def test_p1_scissors_p2_scissors(self):
        self.player_1 = Player("David", "Scissors")
        self.player_2 = Player("Kyle", "Scissors")
        self.game = Game(self.player_1, self.player_2)
        self.game.who_wins(self.player_1, self.player_2)
        self.assertEqual("It's a DRAW, play again!", self.game.who_wins(self.player_1, self.player_2))