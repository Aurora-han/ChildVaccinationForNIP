from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user_db'

    id = db.Column('user_id',db.String(10),primary_key=True)
    password=db.Column('user_id',db.String(20))
    phone=db.Column('user_id',db.String(20))
    name=db.Column('user_id',db.String(20))
    card=db.Column('user_id',db.String(20))
    role=db.Column('user_id',db.Integer())

    def __invert__(self,name):
        self.username=name

    def __repr__(self):
        return "<User '{}'>".format(self.username)
@app.route('/')
def home():
    # users = User.query.all()
    # users
    return '<h1>Hello Woeld!</h1>'+users
if __name__ == '__main__':
    app.run()