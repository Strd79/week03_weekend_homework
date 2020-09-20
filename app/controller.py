from flask import render_template, request
from app import app
from app.models.player import Player
from app.models.game import *

@app.route("/")
def index():
    return render_template("index.html", title="Player 1")

@app.route("/player_1", methods=["POST"])
def player_2s_go():
    player1Name = request.form["name"]
    player1Choice = request.form["choice"]
    player_1 = Player(player1Name, player1Choice)
    return render_template("index2.html", title="Player 2")

@app.route("/player_2", methods=["POST"])
def the_winner_is(player_1, player_2):
    who_wins(player_1, player_2)
    return render_template("index3.html", title="The Winner!")
