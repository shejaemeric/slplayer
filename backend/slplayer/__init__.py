import pymysql
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'sessionSecretKey051!'
app.config['SQLALCHEMY_TRACK_MOSIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/slplayer'

db = SQLAlchemy(app)
CORS(app, resources={r"/*":{"origins":"*"}})

#login manager..............
login_manager = LoginManager()
login_manager.init_app(app)
#........................................


from .user import user
app.register_blueprint(user,url_prefix='/user')

from .track import track
app.register_blueprint(track,url_prefix='/track')

from .auth import auth
app.register_blueprint(auth,url_prefix='/auth')
