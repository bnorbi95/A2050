from flask import Flask
from flask_socketio import SocketIO
from flask_admin import Admin
from gm import GameManager
from flask_sqlalchemy import SQLAlchemy
from config import *
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = secret
app.config['SQLALCHEMY_DATABASE_URI']=DB_ADDRESS
app.config['PRESERVE_CONTEXT_ON_EXCEPTION']=True
db = SQLAlchemy(app)
socketio = SocketIO(app,engineio_logger=False,ping_timeout=30)
admin = Admin(app, name='A2050', template_mode='bootstrap3')
CsrfProtect(app)

gm=GameManager()

import admin
import pages
import socketioutils
