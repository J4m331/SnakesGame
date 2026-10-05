import socket
from functools import wraps
from flask import request, abort
from flask_jwt_extended import verify_jwt_in_request, decode_token
from flask_socketio import join_room, close_room, emit

from App.extensions import socketio


def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return '127.0.0.1'

def is_host_request():
    return request.remote_addr in ('127.0.0.1', '::1')

def jwt_host_only(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not is_host_request():
            abort(403)
        return fn(*args, **kwargs)
    return wrapper
