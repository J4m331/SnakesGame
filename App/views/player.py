from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for, make_response
from flask_jwt_extended import jwt_required, current_user as jwt_current_user, set_access_cookies

from.index import index_views

from App.controllers import (
    create_player,
    get_all_players,
    rename_player,
    create_token
)

player_views = Blueprint('player_views', __name__, template_folder='../templates')

'''
@player_views.route('/player', methods=['POST'])
def create_player_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_player(data['username'])
    return redirect(url_for('player_views.get_user_page'))
'''

@player_views.route('/join', methods=['GET'])
def get_player_action():
    return render_template('join.html')


@player_views.route('/join', methods=['POST'])
def create_player_action():
    data = request.form
    player = create_player(data['username'])
    token = create_token(player.id)
    players = get_all_players()
    response = make_response(render_template('lobby.html', curr_player=player, players=players))
    if not token:
        flash(f"User {data['username']} not created!")
    else:
        flash(f"User {data['username']} created!")
        set_access_cookies(response, token)
    return response

@player_views.route('/rename', methods=['POST'])
@jwt_required()
def rename_player_action():
    data = request.form
    player = jwt_current_user
    players = get_all_players()
    print(player.id)
    rename_player(player.id, data['username'])
    flash(f"User {data['username']} renamed!")
    return render_template('lobby.html', curr_player=player, players=players)
