from flask import session, jsonify
import flask
from . import api
from .. import db
from ..models import User

@api.route('/user/log_in', methods=['POST'])
def user_log_in():
    try:
        username = flask.request.form['username']
        password = flask.request.form['password']
    except:
        return flask.jsonify(status=0);
    user = User.query.filter_by(username=username, password=password).first()
    print dir(user)
    if user is not None:
        return flask.jsonify(
                    status=1,
                    username=username,
                    userID = user.id
                );
    else:
        return flask.jsonify(status=0);

@api.route('/user/register', methods=['POST'])
def user_register():
    print flask.request.form
    username = flask.request.form['username']
    password = flask.request.form['password']
    phoneNumber = flask.request.form['phoneNumber']
    email = flask.request.form['email']

    newUser = User()
    newUser.username = username
    newUser.password = password
    newUser.phoneNumber = phoneNumber
    newUser.email = email

    db.session.add( newUser )
    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify(status=0)

    return jsonify(status=1)
