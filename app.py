from flask import Flask, render_template, request, redirect, flash, session
from boggle import Boggle

boggle_game = Boggle()
BOARD = "board"
app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = "secret"

boggleBoard = boggle_game.make_board()

@app.route("/")
def generate_home():
    """Home page. Generate Board."""

    session[BOARD] = boggleBoard
    board = session.get(BOARD)

    return render_template("home.html", board=board)

@app.route("/guess", methods=["POST"])
def make_guess():

    return redirect("/")
