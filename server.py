#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Flask server frontend for chase
"""

import os
import logging

from logging.handlers import RotatingFileHandler

from flask import Flask, request, jsonify

import search_master

__author__ = "@realdavidawad"


def create_app():
    """
    app factory function
    """
    app = Flask(__name__)
    return app


application = create_app()

# configure logger
logger = logging.getLogger('gunicorn.error')

SEARCH_ENDPOINT = 'search'

SM = search_master.SearchMaster('state_data')


@application.route('/' + SEARCH_ENDPOINT, methods=['GET'])
def search_route():
    """
    main routing for search api
    """
    if not request.data:
        return "Missing params", 422

    keyword = request.json.get('keyword', None)
    state = request.json.get('state', None)

    laws = list(map(str, SM.search(keyword, state)))

    return jsonify({'laws': laws}), 200


if __name__ == '__main__':

    # run the server
    application.run(host='0.0.0.0',
                    port=int(os.environ.get('PORT')),
                    debug=os.environ.get('DEBUG', False),
                    use_reloader=True,
                    threaded=True)
