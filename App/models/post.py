from App.database import db
from datetime import datetime

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'))
    topicId = db.Column(db.Integer, db.ForeignKey('topic.id'))
    text = db.Column(db.String(200), nullable=False) 
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    tags = db.relationship('PostTag', lazy=True, backref="post")
        

    def __repr__(self):
        return f"{self.userId}"

    
    def notifySubscribers(self, subscribers):
        self.text = subscribers


    def toDict(self):
        return {
            "user_id": self.userId,
            "topicId": self.topicId,
            "text": self.text,
            "created": self.created
        }
