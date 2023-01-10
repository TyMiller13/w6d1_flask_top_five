from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favorites')
def top_five():
    basketball_players = ['Allen Iverson', 'Kobe Bryant', 'Michael Jordan', 'Steph Curry', 'Russell Westbrook']
    return render_template('top_five.html', basketball_players=basketball_players)