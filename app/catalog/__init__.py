#flask2/app/catalog/__init__.py

from flask import Blueprint

main=Blueprint('main',__name__,template_folder='templates')

#why is this blueprint importing the route function

from app.catalog import route
