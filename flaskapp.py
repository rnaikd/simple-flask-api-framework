# This library is to be use to make simple rest application
# falskapp.py is main file which understands URL and invoke proper action
# api route must be <host>/api/<classname>/<:param>
# How this will work?
# Let's take some example
# 1. user class
# - To manage users in application, there is a class named User
# - To access that class methods through api first select http method
# - Note: each class will support only 4 methods ['GET','POST','PUT','DELETE']
# - To get user list, api endpoint should be /api/user (http method GET)
# - To get particular user, api endpoint should be /api/user/1
# 2. This application also shows firebase admin auth, so that data can be fetched from firebase and processed
# 3. To change information in apis, change properties in Info() class
# ----------------
# How to use
# Clone the package
# install dependencies
# and try locally
# export FLASK_APP=flaskapp.py
# export FLASK_ENV=development
# python -m flask run

import json

from flask import Flask, url_for, request, Response, jsonify
from markupsafe import escape

from info import Info
from user import User
from auth import Authme


app = Flask(__name__)


@app.route('/')
def index():
    # return info.version
    return "Welcome!"


def seterrorjson(error):
    if 'code' and 'message' not in error:
        return {
                'status': 500,
                'message': 'Something went wrong!'
            }
    else:
        code = error['code']
        param = json.dumps(error['message'])
        info = Info()
        response = {
            'status': code,
            'meta': info.get(),
            'result': param
        }
        return response



def setsuccessjson(param):
    if 'code' and 'data' in param:
        code = param['code']
        param = param['data']
        info = Info()
        response = {
            'status': code,
            'meta': info.get(),
            'result': param
        }
        return response
    return {
            'status': 500,
            'message': 'Something went wrong!!'
        }


@app.route("/api/<path:subpath>", methods=['GET', 'POST', 'PUT', 'DELETE'])
def api(subpath):
    try:
        subpath = escape(subpath).split('/')
        classname = subpath.pop(0)
        classname = classname[0].upper() + classname[1:]
        classmethod = request.method.lower()

        if classname in globals():
            cls = globals()[classname]()
            if hasattr(cls, classmethod) and callable(getattr(cls, classmethod)):
                response = getattr(cls, classmethod)(subpath)
                if 'code' in response and response['code'] in range(199, 210):
                    responsestr = setsuccessjson(response)
                    code = response['code']
                else:
                    if 'code' not in response:
                        response['code'] = 500
                        response['message'] = 'Param code is missing, Something went wrong'
                    responsestr = seterrorjson(response)
                    code = response['code']
            else:
                responsestr = seterrorjson({'code': 404, 'message': 'Resource not found'})
                code = 404
        else:
            responsestr = seterrorjson({'code': 404, 'message': 'Resource not found'})
            code = 404
    except Exception as e:
        return jsonify(e), 500
    else:
        return jsonify(responsestr), code



