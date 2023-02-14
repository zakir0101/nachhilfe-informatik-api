import json
import logging
import os
import traceback

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from flask_cors import CORS
from send_mail_1 import config_mail, create_msg4

from dotenv import load_dotenv


app = Flask(__name__)
UPLOAD_FOLDER = 'files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


project_folder = app.root_path  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
print('domain ', os.environ['DOMAIN'])


@app.route("/")
def get():
    return render_template('index.html', menu="home", lang="de")


@app.route("/<tab>/<lang>")
def get_home(tab, lang):
    return render_template('index.html', menu=tab, lang=lang)


def save_files(request2):
    for file in request2.files.values():
        if file.filename == '':
            print('No selected file')
        else:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))

    pass


def delete_files(request2):
    for file in request2.files.values():
        filename = secure_filename(file.filename)
        os.remove(os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], filename))

    pass


@app.route('/file', methods=['POST'])
def upload_file():
    first_name = request.form['first_name']  #
    last_name = request.form['last_name']  #
    email = request.form['email']  #
    number = request.form.get('number')  #
    interested_in = request.form['interested_in']  #
    how_oft = request.form.get('how_oft')  #
    how_long = request.form.get('how_long')  #
    deadline = request.form.get('deadline')  #
    budget_language = request.form.get('budget_language')
    budget_project = request.form.get('budget_project')

    html_email = render_template('mail.html', **locals())

    mail = config_mail(app)

    try:
        mail.send(create_msg4(app, html_email, first_name, interested_in, request.files.values()))
    except Exception as e:
        logging.error(traceback.format_exc())
        res = dict(type="error");
        return json.dumps(res)
        # return "your request was unfortunately unsuccessful"
    else:
        res = dict(type="success");
        return json.dumps(res)


'''
    <!doctype html>
<title>Upload new File</title>
<h1>hi {request.form['name']} </h1>
<h1>File uploaded successfully</h1> 

'''
if __name__ == '__main__':
    app.run()
