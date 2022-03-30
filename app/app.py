from flask import Flask
from routes.workflow import workflow


app = Flask(__name__)
app.secret_key = 'secret'


app.register_blueprint(workflow, url_prefix="/")
