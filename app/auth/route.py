from flask import render_template,session, request,redirect,url_for
from app.auth.form import registration
from app.auth import authentication as at
from app.auth.models import User
from app import db, bcrypt
from app.catalog import main

@at.route('/register',methods=['GET','POST'])
def register():
    form=registration()
    name=None
    email=None
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']

    return render_template('registration.html',form=form,name=name,email=email)

@at.route('/profile',methods=['GET','POST'])
def profile():
    if not session.get('email')==None:
        name=User.query.filter_by(user_email=session.get('email')).first().user_name
        return render_template('profile1.html',name=name)
    else:
        return redirect('/login')

@at.route('/login',methods=['GET','POST'])
def login():
    message=None
    if request.method=='POST':
        req=request.form
        user=User.query.filter_by(user_email=req['email']).first()
        if user.user_name is None:
            return redirect('/login')
        else:
            if bcrypt.check_password_hash(user.user_password,request.form['password']):
                session['email']=user.user_email
                session['name']=user.user_name
                return redirect('/profile')
            else:
                return render_template('login.html',message='WRONG PASSWORD')
    return render_template('login.html')

@at.route('/sign_up',methods=['GET','POST'])
def signup():
    message=None
    if request.method=='POST':
        req=request.form
        name=req['name']
        email=req['email']
        password=req['password']
        user=User.query.filter_by(user_email=email).first()
        if user is None:
            User.create_user(user=name,email=email,password=password)
            user=User.query.filter_by(user_email=req['email']).first()
            if user.user_name is None:
                return redirect('/login')
            else:
                if bcrypt.check_password_hash(user.user_password,request.form['password']):
                    session['email']=user.user_email
                    session['name']=user.user_name
                    return redirect('/profile')
        else:
            return render_template('sign_up.html',message='email id already exists')
    return render_template('sign_up.html')

@at.route('/signout')
def signout():
    try:
        if not session.get('email')==None:
            session.pop('email')
            session.pop('name')
            return redirect('/index')
        else:
            return redirect('/index')
    except:
        return redirect('/index')
