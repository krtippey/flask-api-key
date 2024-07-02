# -*- coding: utf-8 -*-
"""
"""

# data:: _request_ctx_stack is now data:: flask.globals.request_ctx ... _https://stackoverflow.com/questions/73349956/deprecationwarning-reque-st-ctx-stack-is-deprecated-and-will-be-removed-in-f

from flask import current_app
from werkzeug.local import LocalProxy
from flask.globals import request_ctx

# Magic access to apikey
current_api_key = LocalProxy(lambda: get_api_key())

def get_api_key():
    ak = getattr(request_ctx, 'api_key', None)
    return ak


def get_api_key_manager():
    try:
        return current_app.extensions['flask-api-key']
    except KeyError:
        raise RuntimeError(
            'You must first initializa Flask-API-Key with this'
            'application before using this method.'
        ) from None


def get_ext_config():
    mgr = get_api_key_manager()
    if mgr:
        return mgr.config
