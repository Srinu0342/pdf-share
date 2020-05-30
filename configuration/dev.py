import os
DEBUG=True
SECRET_KEY='topsecret'
SQLALCHEMY_DATABASE_URI='sqlite:///C:\\Users\\bigGs\\Desktop\\flask2\\databases\\BookCatalog.db'
UPLOAD_FOLDER = UPLOAD_FOLDER = os.path.abspath('.\\test_books')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
