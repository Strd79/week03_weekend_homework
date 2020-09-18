from flask import render_template, request
from app import app
from app.models.player import Player
from app.models.game import *

@app.route('/')
def index():
    return render_template("index.html", title="Player 1")

@app.route("/player_1/<player_1_selection>", methods=["POST", "GET"])
def player_2s_go(player_1_selection):
    return render_template("index2.html/player_1_selection", title="Player 2")

@app.route("/player_2/<player_1_selection>/<player_2_selection>", methods=["POST", "GET"])
def the_winner_is(player_1_selction, player_2_selection):
    who_wins(player_1_selction, player_2_selection)
    return render_template("index3.html", title="The Winner!")
