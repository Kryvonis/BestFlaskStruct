from flask_mail import Message, Mail
from app import app

mail = Mail(app)


def send_email(message_string, email):
    """
    function for sending email using settings above
    :param message_string: what message we want to send
    :param email: on what email
    :return: none
    """

    with mail.connect() as conn:  # get server connection
        subject = "Search result in books"
        # create message for sending
        msg = Message(recipients=[email],
                      body=message_string,
                      subject=subject,
                      sender=app.config['MAIL_USERNAME'])
        conn.send(msg)
