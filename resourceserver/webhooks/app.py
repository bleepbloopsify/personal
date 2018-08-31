from os import environ as env

import hmac
from threading import Thread

from flask import Flask, render_template, request, abort

DATA_DIR = env.get('DATA_DIR') or '/mnt/data'
RESUME_SECRET_HASH = sha1(env.get('RESUME_SECRET_TOKEN'))

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/resume', methods='POST')
def resume_hook():

  def verify_signature(payload, signature):
    h = hmac.new(env.get('RESUME_SECRET_TOKEN'), payload, 'sha1')
    recomputed = 'sha1=' + h.hexdigest() # compute hash
    return hmac.compare_digest(recomputed, signature)

  if not verify_signature(request.data, request.headers['X-Hub-Signature']):
    return abort(400)
  
  # TODO: git updates here.

  return 'OK'

if __name__ == '__main__':
  app.run('0.0.0.0', port=env.get('PORT') or 8000)