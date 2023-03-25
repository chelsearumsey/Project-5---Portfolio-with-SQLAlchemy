from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Project Title', db.String())
    date = db.Column('Completion Date', db.String())
    description = db.Column('Description', db.Text)
    skills = db.Column('Skills', db.Text)
    url = db.Column('GitHub Link', db.String())

    def __repr__(self):
        return f'Title: {self.title} Date: {self.date} Project Description: {self.description} Skills: {self.skills}'