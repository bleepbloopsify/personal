from os import environ as env

import hmac
import subprocess

from flask import Flask, render_template, request, abort

DATA_DIR = '/mnt/repos'

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')


@app.route('/resume', methods=['POST'])
def resume_hook():

  def verify_signature(payload, signature):
    h = hmac.new(env.get('RESUME_SECRET_TOKEN').encode('utf-8'), payload, 'sha1')
    recomputed = 'sha1=' + h.hexdigest() # compute hash
    return hmac.compare_digest(recomputed, signature)

  # NOTE: request.data is only accessible with request_type: application/json
  if not verify_signature(request.data, request.headers['X-Hub-Signature']):
    return abort(400)
  
  # TODO: git updates here.

  git_pull(DATA_DIR + '/resume')

  return 'OK'

def git_pull(location):
  subprocess.run(['git', 'pull'], cwd=location)

if __name__ == '__main__':
  app.run('0.0.0.0', port=env.get('PORT') or 8000)