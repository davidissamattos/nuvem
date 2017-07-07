from flask import Flask, redirect, url_for
from flask import render_template
from werkzeug.contrib.fixers import ProxyFix
from sounds.sounds import Sounds
from lightning.lightning import Lightning
import pygame



app = Flask(__name__)
app.config['DEBUG'] = True

#This is to play sounds. It is always initialized and on
pygame.mixer.init()

@app.route('/')
def index():
    output = render_template('index.html')
    return output


@app.route('/rain/')
def rain():
    """ Turn on the lights and sound of rain """
    s = Sounds()
    s.rainsound()

    lightning = Lightning()
    lightning.lightning_rain()

    return redirect(url_for('index'))

@app.route('/rainandthunderstorm/')
def rainandthunderstorm():
    """ Blink lights and sound of strong rain and thunder"""
    s = Sounds()
    s.rainandthunderstorm()

    lightning = Lightning()
    lightning.lightning_rainandthunderstorm()


    return redirect(url_for('index'))

@app.route('/turnon/')
def turnon():
    """ Turn on the lights and a sound of thunder """
    s = Sounds()
    s.thunder_turnon()

    lightning = Lightning()
    lightning.lightning_turnon()

    return redirect(url_for('index'))

@app.route('/turnoff/')
def turnoff():
    """ Turn off the lights and a sound of thunder """
    s = Sounds()
    s.thunder_thurnoff()

    lightning = Lightning()
    lightning.lightning_turnoff()

    return redirect(url_for('index'))

@app.route('/lightrain/')
def lightrain():
    """ Only sound of light rain """
    s = Sounds()
    s.lightrain()

    return redirect(url_for('index'))

app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    #keep_sound_on()
    app.run()
