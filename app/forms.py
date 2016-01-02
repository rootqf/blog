# -*- coding: UTF-8 -*

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class GuestBookForm(Form):
    nickname = StringField('呢称', validators=[DataRequired()])
    text = StringField('内容', validators=[DataRequired()])
    email = StringField('电子邮件', validators=[DataRequired()])
    submit = SubmitField('提交')