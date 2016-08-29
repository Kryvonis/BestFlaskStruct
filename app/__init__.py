from flask import Flask,Blueprint

app = Flask(__name__)

app.config.from_object('config')

# test = Blueprint('test',__name__,template_folder='templates/test')
from app import errors,custom_email_sender

from views import view2
from views import view1
app.register_blueprint(view2.mod)


