from flask_socketio import SocketIO

socketio = SocketIO(ping_interval=5, ping_timeout=5)

LOBBY = "lobby"
HOST = "host"

connectedPlayers = {}