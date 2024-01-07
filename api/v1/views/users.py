#!/usr/bin/python3
'''state API index'''
from api.v1.views import app_views
from flask import jsonify, url_for, redirect, abort, request
from models import storage
from models.user import User


methods_am = ['GET', 'POST', 'DELETE', 'PUT']


@app_views.route("/users", strict_slashes=False, methods=methods_am)
def user_api():
    # get and post
    if request.method == 'GET':
        user_list = []
        for key, value in storage.all(User).items():
            user_list.append(value.to_dict())
        return jsonify(user_list)
