from App.models import Player
from App.database import db
from sqlalchemy.sql.expression import func, select

def create_player(username):
    new_player = Player(username=username)
    db.session.add(new_player)
    db.session.commit()
    return new_player

def get_player(username):
    return db.session.get(Player, username)

def get_all_players():
    return db.session.scalars(db.select(Player)).all()

def get_random_player():
    return db.session.scalars(select(Player).order_by(func.random()).limit(1)).first()

def set_role(username, role):
    player = get_player(username)
    if player:
        player.role = role
        db.session.commit()
        return True
    return None
    
def get_role(username):
    player = get_player(username)
    if player:
        return player.role
    return None
    
def reset_roles():
    players = get_all_players()
    if players:
        for player in players:
            player.role = None
            db.session.commit()
        return True
    return False

def remove_player():
    player = get_player()
    if player:
        db.session.remove(player)
        return True
    return False

def remove_players():
    players = get_all_players()
    if players:
        for player in players:
            db.session.remove(player)
        return True
    return False

def add_score(username, score):
    player = get_player(username)
    if player:
        player.score = player.score + score
        db.session.commit
        return player.score
    return -1

def get_score(username):
    player = get_player(username)
    if player:
        return player.score

def reset_scores():
    players = get_all_players()
    if players:
        for player in players:
            player.score = 0
            db.session.commit
        return True
    return False
        