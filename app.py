from flask import Flask, render_template,request 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friend.db'
#initialize the database
db =SQLAlchemy(app)


#create db model
class Friends(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    #create a function to return the data in the database
    def __repr__(self):
        return '<Name %r>' % self.id

@app.route('/')
def index():

    return render_template("index.html")
@app.route('/about')
def about():
    return render_template("about.html")