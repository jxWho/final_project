from . import api
import flask

@api.app_errorhandler(404)
def api_not_fount(e):
    return flask.jsonify(status=-1, msg="no such api");

@api.app_errorhandler(500)
def internal_server_error(e):
    return flask.jsonify(status=-2, msg="server problem");
