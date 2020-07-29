# User class to demonstrate how this application will work
# Method get is fully configured to get user list and user information from api
# 1. <HOST>/api/user (http method GET) will return
# {
#     "meta": {
#         "author": "Rahul N",
#         "author_email": "naikrahulda@gmail.com",
#         "version": 1
#     },
#     "result": [
#         "User 1",
#         "User 2"
#     ],
#     "status": 200
# }
# 2. <HOST>/api/user/1 (http method GET) will return
# {
#     "meta": {
#         "author": "Rahul N",
#         "author_email": "naikrahulda@gmail.com",
#         "version": 1
#     },
#     "result": "User 2",
#     "status": 200
# }

from __future__ import print_function

from flask import request


class User:
    users = [
        'User 1',
        'User 2'
    ]

    def get(self, param):
        if len(param) > 1:
            return {
                'code': 400,
                'message': 'Wrong number of params'
            }

        data = self.users

        if len(param) is 1:
            data = data[int(param[0])]

        return {
                'code': 200,
                'data': data
            }

    def post(self, param):
        requestparam = request.form

        if 'name' not in requestparam:
            return {
                'code': 400,
                'message': 'name is required'
            }
        if 'number' not in requestparam:
            return {
                'code': 400,
                'message': 'number is required'
            }
        if requestparam['name'] == '':
            return {
                'code': 400,
                'message': 'name can not be empty'
            }
        if requestparam['number'] == '':
            return {
                'code': 400,
                'message': 'number can not be empty'
            }

        data = {
            'body': requestparam['name'],
            'number': requestparam['number']
        }

        return {
                'code': 200,
                'data': data
            }


    def put(self, param):
        return {
            'code': 201,
            'data': param
        }

    def delete(self, param):
        return {
            'code': 200,
            'data': param
        }
