# -*- coding: UTF-8 -*-


from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views, models, jsontest

# def add_cors_header(response):
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'
#     response.headers['Access-Control-Allow-Methods'] = 'POST, GET, PUT, PATCH, DELETE, OPTIONS'
#     return response
#
# app.after_request(add_cors_header)


