from flask import render_template, request, redirect
from app import app
from app.models.player import *
from app.models.game import *
from app.models.players import player1, player2



@app.route ('/')
def index():
    return render_template('index.html', title='Home', player=player)

@app.route ('/<choice1>/<choice2>')
def game_winner(choice1, choice2):
    first_game(player1, player2)
    return render_template('game_winner.html', title='winner', winner=first_game)

# A route in a controller that takes in two wildcards e.g. (/<hand1>/<hand2>)

# A player class that takes in a name and the hand that was played, e.g. Player("player 1", hand1)

# A function to check which player won based on what was picked in the url path(passed into the 
# route in the controller), (it will return: paper beats rock, scissors draws with scissors.) e.g. check_win(player1, player2)