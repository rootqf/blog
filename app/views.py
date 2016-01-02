# -*- coding: UTF-8 -*-

from flask import render_template, redirect
from app import app
from forms import GuestBookForm
from models import db, GuestBook


@app.route('/guestbook', methods=['GET', 'POST'])
def guestbook():
    form = GuestBookForm()
    if form.validate_on_submit():
        nickname = form.nickname.data
        text = form.text.data
        email = form.email.data
        guesttext = GuestBook(nickname, text, email)
        db.session.add(guesttext)
        db.session.commit()
        return redirect('/guestbook')

    # guestbook = GuestBook.query.all()
    # guestbook = GuestBook.query.filter_by(id=2).first()
    guestbook = GuestBook.query.filter_by(id=2)
    # guestbook = GuestBook.query.filter_by(nickname='aaa1')
    return render_template('guestbook.html', title='留言簿', form=form, guestbook=guestbook)
