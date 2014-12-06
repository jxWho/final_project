from flask import session, jsonify
import flask
from . import api
from .. import db

@api.route('/user/log_in', methods=['GET', 'POST'])
def user_log_in():
    return flask.jsonify(status=1);
