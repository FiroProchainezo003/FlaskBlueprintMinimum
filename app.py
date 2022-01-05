from flask import Flask, render_template
from views.app1 import App1
from views.app2 import App2

app = Flask(__name__)

app.register_blueprint(App1, url_prefix="/app1")
app.register_blueprint(App2, url_prefix="/app2")


@app.route('/')
def hello_world():
    return render_template('views/index.html')


if __name__ == '__main__':
    app.run()
