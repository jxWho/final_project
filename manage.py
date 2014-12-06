#!./venv/bin/python

import os
from app import create_app, db
from flask.ext.script import Manager, Shell

app = create_app('default')
manager = Manager( app )

if __name__ == '__main__':
    manager.run()
