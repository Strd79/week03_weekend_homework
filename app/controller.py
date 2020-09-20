from flask import render_template, request
from app import app
from app.models.player import *
from app.models.game import *

@app.route("/")
def index():
    return render_template("index.html", title="Player 1")

@app.route("/player_1", methods=["POST"])
def player_2s_go():
    player1Name = request.form["name1"]
    player1Choice = request.form["choice1"]
    player_1 = Player(player1Name, player1Choice)
    Game.add_player(player_1)
    return render_template("index2.html", title="Player 2")

@app.route("/player_2", methods=["POST"])
def the_winner_is():
    player2Name = request.form["name2"]
    player2Choice = request.form["choice2"]
    player_2 = Player(player2Name, player2Choice)
    Game.add_player(player_2)
    result = Game.who_wins(Game.players)
    return render_template("index3.html", title="The Winner!", result=result)
