import click, sys
from flask.cli import with_appcontext, AppGroup
from flask import jsonify

from App.database import db
from App.models import User
from App.main import create_app, socketio
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize, get_all_questions, get_local_ip )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()


# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')
    
@app.cli.command("ip", help="Displays local ip")
def ip():
    print(get_local_ip())

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())
        
@user_cli.command("list_questions", help="Lists questions in the database")
@click.argument("format", default="string")
def list_question_command(format):
    ques = get_all_questions()
    print(jsonify(ques))

app.cli.add_command(user_cli) # add the group to the cli