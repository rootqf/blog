#!flask/bin/python
# -*- coding: UTF-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf8')

from app import app
# from app.models import db
# db.create_all()
app.run(host='0.0.0.0', debug=True)
