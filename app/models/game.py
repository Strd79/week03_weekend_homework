from app.models.player import Player

class Game:
    
    def __init__(self, input_player_1, input_player_2):
        self.player_1 = input_player_1
        self.player_2 = input_player_2

    def who_wins(self, player_1, player_2):
        if self.player_1.choice == "Rock" and self.player_2.choice == "Scissors":
            return f"Player 1 WINS with {self.player_1.choice}!"
        elif self.player_1.choice == "Rock" and self.player_2.choice == "Paper":
            return f"Player 2 WINS with {self.player_2.choice}!"
        elif self.player_1.choice == "Paper" and self.player_2.choice == "Rock":
            return f"Player 1 WINS with {self.player_1.choice}!"
        elif self.player_1.choice == "Paper" and self.player_2.choice == "Scissors":
            return f"Player 2 WINS with {self.player_2.choice}!"
        elif self.player_1.choice == "Scissors" and self.player_2.choice == "Paper":
            return f"Player 1 WINS with {self.player_1.choice}!"
        elif self.player_1.choice == "Scissors" and self.player_2.choice == "Rock":
            return f"Player 2 WINS with {self.player_2.choice}!"
        else:
            return "It's a DRAW, play again!"
        