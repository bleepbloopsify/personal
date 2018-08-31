from os import environ as env
from threading import Thread

from flask import Flask

DATA_DIR = env.get('DATA_DIR') or '/mnt/data'

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run('0.0.0.0', port=env.get('PORT') or 8000)