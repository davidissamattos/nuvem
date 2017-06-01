from flask import Flask
from flask import render_template
from werkzeug.contrib.fixers import ProxyFix
from sounds.sounds import Sounds
from lightning.lightning import Lightning
import pygame


app = Flask(__name__)
#This is to play sounds. It is always initialized and on
pygame.mixer.init()

@app.route('/')
def index():
    s = Sounds()
    s.testsound()
    output = render_template('index.html')
    return output




app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    app.run()
