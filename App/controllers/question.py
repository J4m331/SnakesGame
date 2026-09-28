from App.models import Question
from App.database import db
from sqlalchemy.sql.expression import func, select
import json

def create_question(question, answerA, answerB, answerC, correctAnswer):
    question = Question(question,answerA,answerB,answerC,correctAnswer)
    db.session.add(question)
    db.session.commit()
    return question

def add_question(question, answerA, answerB, answerC, correctAnswer):
    question = Question(question,answerA,answerB,answerC,correctAnswer)
    db.session.add(question)
    return question

def get_random_question():
    return db.session.scalars(select(Question).order_by(func.random()).limit(1)).first()

def get_all_questions():
    return db.session.scalars(db.select(Question)).all()

def answer_question(question):
    questionAnswered = db.session.get(Question, question)
    if questionAnswered:
        questionAnswered.answered = True
        db.session.commit()
        return questionAnswered.answered
    return False

def load_questions(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        create_question(
            item["question"],
            item["answerA"],
            item["answerB"],
            item["answerC"],
            item["correctAnswer"],
        )