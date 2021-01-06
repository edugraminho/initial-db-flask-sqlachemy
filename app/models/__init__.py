from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
    surname = db.Column(db.String, unique=False, nullable=True)
    document = db.Column(db.String(1024), unique=True, nullable=False)
    
    accounts = db.relationship("CCAccount", back_populates="user")
    

    def __repr__(self):
        return f'<User {self.name} {self.document}>'

# class CCAccount(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     agency = db.Column(db.String, nullable=False)
#     number = db.Column(db.String, nullable=False)
#     money = db.Column(db.Float, nullable=False)
    
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
#     user = db.relationship("User", back_populates="accounts")