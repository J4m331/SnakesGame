from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_db():
    db.create_all()
    
def init_db(app):
    db.init_app(app)