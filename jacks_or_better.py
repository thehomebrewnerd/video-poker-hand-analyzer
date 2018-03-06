from flask import Flask
from flask import request
from flask import render_template
from card import Card
from hand import Hand
from score import score_hand
from analyze import analyze_hand

app = Flask(__name__)

@app.route('/')
def pick_hand():

    rank_dict = {
        2:'2',
        3:'3',
        4:'4',
        5:'5',
        6:'6',
        7:'7',
        8:'8',
        9:'9',
        10:'T',
        11:'J',
        12:'Q',
        13:'K',
        14:'A',
    }

    suits = ['C', 'D', 'H', 'S']
    ranks = [rank_dict[num] for num in range(2,15)]

    context = {
        'suits':suits,
        'ranks':ranks,
    }
    return render_template('pick_hand.html', **context)

@app.route('/<hand_string>')
def analyze(hand_string):
    rank_dict = {
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
        'T':10,
        'J':11,
        'Q':12,
        'K':13,
        'A':14,
    }

    cards = hand_string.split('-')
    card_list = [Card(card[1], rank_dict[card[0]]) for card in cards]
    hand = Hand(card_list)
    score = score_hand(hand)
    hand_to_hold = analyze_hand(hand)
    hold_cards = [str(card) for card in hand_to_hold.cards]
    context = {'cards':cards, 'score':score, 'hold_cards':hold_cards}
    return render_template('analyze.html', **context)

app.run(debug=True)
