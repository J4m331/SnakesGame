from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (
    create_player,
    get_all_players,
    jwt_required
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/player', methods=['POST'])
def create_player_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_player(data['username'], data['password'])
    return redirect(url_for('user_views.get_user_page'))
