#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import requests
import logging
import json
import traceback


from sys import argv
from datetime import datetime
from flask import Flask, request, jsonify
from time import strftime
from logging.handlers import RotatingFileHandler


import searcher

__author__ = "@realdavidawad"

def create_app(config_filename=None):
    app = Flask(__name__)
    return app

application = create_app()

# configure logger
logger = logging.getLogger('gunicorn.error')

# will happen before every request made to lobe.
#  @application.before_request
#  def before_request():
    #  return

SEARCH_ENDPOINT = 'search'


@application.route('/' + SEARCH_ENDPOINT, methods=['GET'])
def search_route():

    application.logger.debug('RECEIVED REQUEST')

    if not request.data: return "Missing keyword param", 422
    keyword = request.json.get('keyword', None)
    print(request.json, keyword)

    return jsonify(searcher.search_keyword(keyword)), 200


if __name__ == '__main__':

    # set logger
    application.logger.handlers.extend(gunicorn_error_logger.handlers)
    application.logger.setLevel(logging.DEBUG)
    application.logger.debug('this will show in the log')

    # maxBytes to small number, in order to demonstrate the generation of multiple log files (backupCount).
    #  handler = RotatingFileHandler('lobe.log', maxBytes=10000, backupCount=3)
    #  # getLogger(__name__):   decorators loggers to file + werkzeug loggers to stdout
    #  # getLogger('werkzeug'): decorators loggers to file + nothing to stdout
    #  # logger = logging.getLogger(__name__)
    #  logger.setLevel(logging.ERROR)
    #  logger.addHandler(handler)


    # run the server
    application.run(host = '0.0.0.0',
            port         = int(os.environ.get('PORT')),
            debug        = os.environ.get('DEBUG', False),
            use_reloader = True,
            threaded     = True)
