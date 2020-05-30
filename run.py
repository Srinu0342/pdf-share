from app import create_app,db
from app.auth.models import User

#from app import meta and engine


flask_app=create_app('prod')
#meta.create_all(engine)
with flask_app.app_context():#study this
    db.create_all()
flask_app.run(port=8080)
