# -*- coding: UTF-8 -*-


from app import app
from datetime import timedelta
from flask import jsonify, current_app, request, make_response
from functools import update_wrapper


def allow_origin(f):
    from functools import wraps
    from flask import make_response

    @wraps(f)
    def wrapped(*args, **kwargs):
        rv = f(*args, **kwargs)
        response = make_response(rv)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    return wrapped


def allow_cross_domain(fun):
    from functools import wraps
    from flask import make_response

    @wraps(fun)
    def wrapper_fun(*args, **kwargs):
        rst = make_response(fun(*args, **kwargs))
        rst.headers['Access-Control-Allow-Origin'] = '*'
        rst.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
        allow_headers = "Referer,Accept,Origin,User-Agent"
        rst.headers['Access-Control-Allow-Headers'] = allow_headers
        return rst

    return wrapper_fun


@app.route('/testjson', methods=['GET'])
# @allow_cross_domain
@allow_origin
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


@app.route('/jsonpost1', methods=['GET', 'POST', 'OPTIONS'])
@allow_origin
def test_json_post():
    from flask import request, abort
    print request.json
    if not request.json:
        abort(400)
    task = {
        'id': request.json['id'],
        'nickname': request.json.get('nickname')
    }
    return jsonify({'task': task}), 201


@app.route('/jsonpost', methods=['GET', 'POST', 'OPTIONS'])
def jsonpost():
    from flask import request
    print request.args
    callback = request.args.get('callback', False)
    request_id = request.args.get('id')
    request_nickname = request.args.get('nickname')
    str_json = callback + "({'id':" + request_id + ", 'nickname':" + request_nickname + "})"
    print str_json
    # return "%s({'a':1, 'b':2 })" % callback
    return str_json
