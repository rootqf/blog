# -*- coding: UTF-8 -*-

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'dataSqlite.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
db = SQLAlchemy(app)

class GuestBook(db.Model):
    __tablename__ = 'guestbook'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(40), index=True, nullable=False)
    text = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(50), index=True)

    def __init__(self, nickname, text, email):
        self.nickname = nickname
        self.text = text
        self.email = email

    def __repr__(self):
        return '<nickname %r>' % self.nickname