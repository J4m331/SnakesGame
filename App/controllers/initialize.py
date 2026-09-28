from .player import create_player
from .question import load_questions
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_player('alice')
    create_player('bob')
    create_player('charles')
    create_player('dave')
    create_player('eve')
    load_questions("questions.json")
