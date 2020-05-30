import os
from app.catalog import main
from flask import render_template,redirect,request,url_for,send_from_directory,session
from werkzeug.utils import secure_filename
from app.catalog.models import pdf_storage


ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
from configuration.prod import UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/')
@main.route('/index')
def hello():
    return render_template('welcomepage.html',user=session.get('name'))

@main.route('/bookupload',methods=['GET','POST'])
def book_upload():
    if request.method == 'POST':
        if not session.get('name')==None:
            # check if the post request has the file part
            if 'file' not in request.files:
                print('No file part')
                return str(request.files)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                print('No selected file')
                return redirect(request.url)

            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                pdf_storage.create_storage(user=session.get('name'),filename=filename)
                file.save(os.path.join(UPLOAD_FOLDER, filename))
                return redirect('/bookupload')
            else:
                return redirect(request.url)
        else:
            return redirect('/login')
    else:
        if not session.get('name')==None:
            library=pdf_storage.query.filter_by(user=session.get('name')).all()
            return render_template('bookupload.html',library=library)
        else:
            return redirect('/login')

@main.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER,filename)
