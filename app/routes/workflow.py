from flask import Blueprint, render_template


workflow = Blueprint("workflow", __name__, static_folder="static", template_folder="templates")


@workflow.route('/home')
@workflow.route('/')
def home():
    return render_template('home.html')
