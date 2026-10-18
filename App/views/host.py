from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

host_views = Blueprint('host_views', __name__, template_folder='../templates')

from App.controllers import (
    jwt_host_only,
    get_local_ip,
    get_player,
    get_all_players,
    remove_player,
    reset_scores
)

import io
import qrcode
import base64

from App.extensions import socketio, HOST, connectedPlayers
from App.socket_events import roster

@host_views.route('/host', methods=['GET'])
@jwt_host_only
def host_page():
    players = get_all_players()
    return render_template('host.html', qrcode=get_qrcode(), ip=f"http://{get_local_ip()}:5000", players=players)

@host_views.route('/rm_player/<int:ID>', methods=['DELETE'])
@jwt_host_only
def remove_player_action(ID):
    sids = [sid for sid, pid in connectedPlayers.items() if pid == ID]

    if not remove_player(ID):
        return 'Player not found', 404

    for sid in sids:
        socketio.emit('player_removed', to=sid)
        connectedPlayers.pop(sid, None)

    socketio.emit('roster', roster(), to=HOST)
    return '', 204

@host_views.route('/rs_player_scores', methods=['POST'])
@jwt_host_only
def reset_player_scores_action():
    reset_scores()
    socketio.emit('roster', roster(), to=HOST)
    return ''

def get_qrcode():
    local_ip = get_local_ip()
    port = 5000
    join_url = f"http://{local_ip}:{port}"
    
    qrcodelink = qrcode.QRCode(box_size=10, border=1)
    qrcodelink.add_data(join_url)
    qrcodelink.make(fit=True)
    img = qrcodelink.make_image(fill_color="black", back_color="white")
    
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    qr_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return qr_base64
