from flask import Blueprint, redirect, render_template, jsonify
from flask_jwt_extended import jwt_required

index_views = Blueprint('index_views', __name__, template_folder='../templates')

from App.controllers import is_host_request, get_local_ip

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html', is_host=is_host_request(), ip=get_local_ip())

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})