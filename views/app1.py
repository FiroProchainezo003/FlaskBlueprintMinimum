from flask import Blueprint, render_template

App1 = Blueprint('app1', __name__)


@App1.route('/')
def index():
    return render_template('views/app1.html')
