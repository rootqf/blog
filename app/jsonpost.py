# -*- coding: UTF-8 -*-

from flask import jsonify, request, abort, make_response, current_app
import simplejson as simplejson
from functools import wraps
from app import app

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def allow_cross_domain(fun):
    # from functools import wraps
    # from flask import make_response

    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst

    return wrapper_fun


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


@app.route('/testjson')
@allow_cross_domain
def testjson():
    tasks = [
        {
            'id': 1,
            'title': u'Buy groceries',
            'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
            'done': False
        },
        {
            'id': 2,
            'title': u'Learn Python',
            'description': u'Need to find a good Python tutorial on the web',
            'done': False
        }
    ]
    return jsonify({'tasks': tasks})


@app.route('/jsonpost', methods=['POST'])
def jsonp(func):
    """Wraps JSONified output for JSONP requests."""

    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)

    return decorated_function


def jsonpost():
    if not request.json:
        abort(400)
    callback = request.args.get('callback', False)
    task = {'id': request.json['id'], 'nickname': request.json['nickname']} + ")"
    print task
    # return jsonify({'tasks': task})
    # return HttpResponse(simplejson.dumps({"jsonp": false,"aa": "callbackName"}))
    return task


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
