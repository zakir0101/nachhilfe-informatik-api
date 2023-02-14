from flask_mail import Mail, Message
import os

from werkzeug.utils import secure_filename


def config_mail(app):
    mail_settings = {
        "MAIL_SERVER": 'smtp-mail.outlook.com.',
        "MAIL_PORT": 587,
        "MAIL_USE_TLS": True,
        "MAIL_USE_SSL": False,
        "MAIL_USERNAME": os.environ['EMAIL_USERNAME1'],
        "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD1']
    }
    app.config.update(mail_settings)
    mail = Mail(app)
    return mail


def create_msg1():
    msg = Message('Hello from the other side!', sender=os.environ['EMAIL_USERNAME'], recipients=['zakir1996@gmail.com'])
    msg.body = "Hey Paul, sending you this email from my Flask app, lmk if it works"
    # msg.msgId = msg.msgId.split('@')[0] + 'http://127.0.0.1:5000/about%20us'  # for instance your domain name
    return msg


def create_msg2(app):
    msg = Message('Hello from the other side!', sender=os.environ['EMAIL_USERNAME'], recipients=['zakir1996@gmail.com'])
    msg.html = "<b>Hey Paul</b>, sending you this email from my <a href=https://google.com >  " \
               "Flask app</a>, lmk if it works"
    # msg.msgId = msg.msgId.split('@')[0] + 'http://127.0.0.1:5000/about%20us'  # for instance your domain name
    with app.open_resource(os.path.join(app.root_path, "files", "google-icon.png")) as fp:
        msg.attach("google-icon.png", "image/png", fp.read())
    return msg


def create_msg3(app, name, user_msg, files):
    msg = Message("new Customer has arrived", sender=os.environ['EMAIL_USERNAME'],
                  recipients=[os.environ['EMAIL_USERNAME']])
    msg.html = f"<h1 style='text-align: center'>{name}</h1> \
                <p style='color:cornflowerblue'>{user_msg}</p>"
    for f in files:
        # msg.msgId = msg.msgId.split('@')[0] + 'http://127.0.0.1:5000/about%20us'  # for instance your domain name
        f_name = secure_filename(f.filename)
        msg.attach(filename=f_name, content_type=f.mimetype, data=f.stream.read())

    return msg


def create_msg4(app, msg_html, first_name, interested_in,  files):
    msg = Message(f"{first_name}, interested in {interested_in}",
                  sender=os.environ['EMAIL_USERNAME1'],
                  recipients=[os.environ['EMAIL_USERNAME1']])
    msg.html = msg_html
    for f in files:
        print(f.filename)
        f_name = secure_filename(f.filename)
        msg.attach(filename=f_name, content_type=f.mimetype, data=f.stream.read())

    return msg
