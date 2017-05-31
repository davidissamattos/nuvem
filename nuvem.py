from flask import Flask
from werkzeug.contrib.fixers import ProxyFix

from sounds.sounds import Sounds
from lightning.lightning import Lightning


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'




app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run()
