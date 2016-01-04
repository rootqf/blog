# -*- coding: UTF-8 -*-

from flask import render_template, redirect, url_for
from app import app
from forms import GuestBookForm
from models import db, GuestBook


@app.route('/guestbook/delete/<gbid>')
def guestbook_delete(gbid):
    """
    根据gbid主键值删除数据
    """
    getdata = GuestBook.query.filter_by(id=gbid).first()
    if not getdata is None:
        db.session.delete(getdata)
        db.session.commit()
    return redirect(url_for('guestbook'))


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
        return redirect(url_for('guestbook'))

    # 删除数据
    # getdata = GuestBook.query.filter_by(id=3).first()
    # if not getdata is None:
    #     db.session.delete(getdata)
    #     db.session.commit()

    # 查询数据
    guestbook = GuestBook.query.all()
    # guestbook = GuestBook.query.filter_by(id=2).first()
    # guestbook = GuestBook.query.filter_by(nickname='aaa1')

    # 修改数据
    # guestbook = GuestBook.query.filter_by(id=2).first()
    # guestbook.nickname='aaa2'
    # guestbook.email='aaa2@qq.com'
    # db.session.add(guestbook)
    # db.session.commit()

    # 批量修改数据
    # guestbook = GuestBook.query.all()
    # for data in guestbook:
    #     if data.id == 2:
    #         data.nickname = data.nickname+'3'
    #         db.session.add(data)
    #         db.session.commit()

    return render_template('guestbook.html', title='留言簿', form=form, guestbook=guestbook)
