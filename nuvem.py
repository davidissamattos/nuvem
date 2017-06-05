from flask import Flask
from flask import render_template
from werkzeug.contrib.fixers import ProxyFix
from sounds.sounds import Sounds
from lightning.lightning import Lightning
import pygame

#for keeping the sound on
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from sounds.sounds import Keepsoundon
import atexit

app = Flask(__name__)
#This is to play sounds. It is always initialized and on
pygame.mixer.init()

def keep_sound_on():
    scheduler = BackgroundScheduler()
    scheduler.start()
    scheduler.add_job(
        func=Keepsoundon,
        trigger=IntervalTrigger(seconds=11),
        id='sound_on',
        name='Keep sound on by pulsing an unaudible beep to the speakers every 60s',
        replace_existing=True)
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())

@app.route('/')
def index():
    s = Sounds()
    s.testsound()
    output = render_template('index.html')
    return output



app.wsgi_app = ProxyFix(app.wsgi_app)
if __name__ == '__main__':
    #keep_sound_on()
    app.run()
