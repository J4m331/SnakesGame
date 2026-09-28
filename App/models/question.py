from App.database import db

class Question(db.Model):
    qID = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(128), nullable=False, unique=True)
    answerA = db.Column(db.String(64), nullable=False)
    answerB = db.Column(db.String(64), nullable=False)
    answerC = db.Column(db.String(64), nullable=False)
    correctAnswer = db.Column(db.Integer, nullable=False)
    answered = db.Column(db.Boolean, default=False)
    
    def __init__(self, question, answerA, answerB, answerC, correctAnswer):
        self.question = question
        self.answerA = answerA
        self.answerB = answerB
        self.answerC = answerC
        self.correctAnswer = correctAnswer