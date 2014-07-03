from app import app
import flask
from flask import render_template
from flask import request
from flask import Response
from flask import abort

from simplejson import JSONDecodeError

import json
import requests
import urllib

from settings import slack_key
import re

#slack_webhook = 'https://dssg.slack.com/services/hooks/incoming-webhook?token={slack_key}'
w3w_base = 'http://w3w.co/'
w3w_api = 'http://api.what3words.com/w3w'

is_three_word = re.compile('^\w+?\.\w+?\.\w+$')

@app.route('/receive', methods=['POST'])
def slack_receive():
#========================================================================
# return w3w link
##===========================================================================
    
    msg = request.form['text']
    chunks = [x.strip() for x in msg.split()]

    responses = []
    for token in chunks:

        if is_three_word.match(token):
            # send link
            response_text = '<{}>'.format(w3w_base + token)
            responses.append(response_text)

    return Response(json.dumps({'text': '\n'.join(responses)}))


