import os

DEBUG=False
SECRET_KEY='topsecret'
SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
UPLOAD_FOLDER = 'C:\\Users\\bigGs\\Desktop\\flask2\\books'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
