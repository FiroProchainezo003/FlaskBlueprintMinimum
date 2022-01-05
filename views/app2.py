from flask import Blueprint, render_template

App2 = Blueprint('app2', __name__)


@App2.route('/')
def index():
    return render_template('views/app2.html')
