from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for, make_response
from flask_jwt_extended import jwt_required, current_user as jwt_current_user, set_access_cookies, get_current_user, verify_jwt_in_request
from App.extensions import socketio

from.index import index_views

from App.controllers import (
    create_player,
    get_all_players,
    get_player_by_username,
    rename_player,
    create_token,
    set_online
)

from App.socket_events import roster

HOST="host"

player_views = Blueprint('player_views', __name__, template_folder='../templates')

def get_current_token():
    try:
        verify_jwt_in_request(optional=True)
        return get_current_user()
    except Exception:
        return None

@player_views.route('/join', methods=['GET'])
def get_player_action():
    if get_current_token():
        return redirect(url_for('player_views.lobby'))
    return render_template('join.html')


@player_views.route('/join', methods=['POST'])
def create_player_action():
    if get_current_token():
        return redirect(url_for('player_views.lobby'))
    
    data = request.form
    if (get_player_by_username(data['username'])):
        flash(f"User {data['username']} already created!")
        return render_template('join.html')
    else:
        player = create_player(data['username'])
        token = create_token(player.id)
        players = get_all_players()
        response = make_response(redirect(url_for('player_views.lobby')))
        if not token:
            flash(f"User {data['username']} not created!")
        else:
            flash(f"User {data['username']} created!")
            set_access_cookies(response, token)
        socketio.emit('roster', roster(), to=HOST)
        return response

@player_views.route('/rename', methods=['POST'])
@jwt_required()
def rename_player_action():
    data = request.form
    player = jwt_current_user
    print(player.id)
    rename_player(player.id, data['username'])
    flash(f"User {data['username']} renamed!")
    return redirect(url_for('player_views.lobby'))

@player_views.route('/lobby', methods=['GET'])
def lobby():
    player_token = get_current_token()
    if player_token is None:
        return redirect(url_for('player_views.get_player_action'))
    return render_template('lobby.html', curr_player=jwt_current_user, players=get_all_players())