# flask2/app/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

csrf=CSRFProtect()
db=SQLAlchemy()
#login_manager=LoginManager()
bcrypt=Bcrypt()

from app.catalog import models
from app.auth import models


#flask app at local level is created;
def create_app(config_type):#app factory
    app=Flask(__name__)
    configuartion=os.path.join(os.getcwd(),'configuration',config_type+'.py')
    app.config.from_pyfile(configuartion)  #app configuartion

    db.init_app(app)
    bcrypt.init_app(app)
    #login_manager.init_app(app)      #binding app to these objects for database and login security
    csrf.init_app(app)

    from app.catalog import main        #app is the directory app
    app.register_blueprint(main)        #app is the flask application app

    from app.auth import authentication as at
    app.register_blueprint(at)

    @app.errorhandler(404)
    def error(e):
        return '<h2>Error 404: Page not found</h2>'

    return app
