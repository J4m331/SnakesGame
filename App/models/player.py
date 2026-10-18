from App.database import db

class Player(db.Model):
    __table_args__ = {'sqlite_autoincrement': True}
    
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(32), nullable=False)
    role = db.Column(db.String(16))
    score = db.Column(db.Integer, default=0)
    profileimg = db.Column(db.LargeBinary)
    currentAnswer = db.Column(db.Integer)
    online = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, username):
        self.username = username

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'score': self.score,
            'online': self.online
        }

