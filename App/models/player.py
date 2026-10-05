from App.database import db

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(32), nullable=False, unique=True)
    role = db.Column(db.String(16))
    score = db.Column(db.Integer, default=0)
    profileimg = db.Column(db.LargeBinary)
    currentAnswer = db.Column(db.Integer)
    online = db.Column(db.Boolean)

    def __init__(self, username):
        self.username = username

    def get_json(self):
        return{
            'username': self.username,
            'role': self.role
        }

