# -*- coding: UTF-8 -*

# flask.ext.wtf换为flask_wtf
# from flask.ext.wtf import Form
from flask_wtf import Form
from wtforms import StringField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class GuestBookForm(Form):
    nickname = StringField('呢称', validators=[DataRequired()])
    text = TextAreaField('内容', validators=[DataRequired()])
    email = StringField('电子邮件', validators=[DataRequired()])
    submit = SubmitField('提交')

