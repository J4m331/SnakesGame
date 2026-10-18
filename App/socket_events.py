from flask import request, current_app
from flask_socketio import emit, join_room, leave_room
from flask_jwt_extended import verify_jwt_in_request, get_current_user

from .extensions import socketio, HOST, LOBBY, connectedPlayers

from App.controllers import(
    set_online,
    remove_online,
    get_all_players
)

def roster():
    return [p.get_json() for p in get_all_players()]

@socketio.on("connect")
def handle_connect():
    try:
        verify_jwt_in_request(optional=True)
    except Exception:
        pass
    
    player = get_current_user()
        
    if player is None:
        join_room(HOST)
        emit('roster', roster(), to=request.sid)
        return
    
    connectedPlayers[request.sid] = player.id
    set_online(player.id)
    join_room(LOBBY)
    print("CONNECT", request.sid, player.username if player else "HOST", player.id)
    emit('roster', roster(), to=HOST)
    
@socketio.on("disconnect")
def handle_disconnect():
    player_id = connectedPlayers.pop(request.sid, None)
    
    if player_id is None:
        return
    
    if player_id not in connectedPlayers.values():
        #with current_app.app_context():
            remove_online(player_id)
    emit('roster', roster(), to=HOST)