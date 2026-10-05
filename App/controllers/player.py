from App.models import Player
from .host import get_local_ip
from App.database import db
from sqlalchemy.sql.expression import func, select
from flask_socketio import join_room, close_room

def create_player(username):
    new_player = Player(username=username)
    db.session.add(new_player)
    db.session.commit()
    return new_player

def rename_player(id, newname):
    player = get_player(id)
    if player:
        player.username = newname
        db.session.commit()
        return True
    return None

def get_player(id):
    return db.session.get(Player, id)

def get_all_players():
    return db.session.scalars(db.select(Player)).all()

def get_random_player():
    return db.session.scalars(select(Player).order_by(func.random()).limit(1)).first()

def set_role(id, role):
    player = get_player(id)
    if player:
        player.role = role
        db.session.commit()
        return True
    return None
    
def get_role(id):
    player = get_player(id)
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

def remove_player(id):
    player = get_player(id)
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

def add_score(id, score):
    player = get_player(id)
    if player:
        player.score = player.score + score
        db.session.commit
        return player.score
    return -1

def get_score(id):
    player = get_player(id)
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

def set_online(id):
    player = get_player(id)
    if player:
        player.online = True
        db.session.commit
        return True
    return False

def remove_online(id):
    player = get_player(id)
    if player:
        player.online = False
        db.session.commit
        return True
    return False
