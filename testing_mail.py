import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import requests as requests
from flask import Flask

from dotenv import load_dotenv

project_folder = os.path.expanduser('./')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
print('domain ', os.environ['DOMAIN'])


def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/" + os.environ['DOMAIN'] + "/messages",
        auth=("api", os.environ['API_KEY']),
        data={"from": "Excited User <mailgun@" + os.environ['DOMAIN'] + ">",
              "to": [os.environ["EMAIL_USERNAME1"], os.environ["EMAIL_USERNAME2"],
                     "zakir.elkheir@gmail.com", ],
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})


def sendgrid_test():
    message = Mail(from_email='learn-programming-online@outlook.com',
                   to_emails=['learn-programming-online@outlook.com','zakir1996@gmail.com'],
                   subject='Sending with Twilio SendGrid is Fun',
                   html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


sendgrid_test()
