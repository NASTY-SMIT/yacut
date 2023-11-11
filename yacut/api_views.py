from re import match

from flask import jsonify, request

from . import app, db
from .constants import (
    NOT_FOUND_ID, MISSING_BODY, URL_REQUIRED,
    LINK_DUPLICATE, INVALID_NAME)
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_opinion(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if not url_map:
        raise InvalidAPIUsage(NOT_FOUND_ID, 404)
    return jsonify({'url': url_map.original}), 200


@app.route('/api/id/', methods=['POST'])
def add_short_link():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage(MISSING_BODY)
    if data.get('url') is None:
        raise InvalidAPIUsage(URL_REQUIRED)
    custom_id = data.get('custom_id')
    if custom_id and URLMap.query.filter_by(short=custom_id).first() is not None:
        raise InvalidAPIUsage(LINK_DUPLICATE)
    if not custom_id:
        data['custom_id'] = get_unique_short_id()
    elif not match(r'^[A-Za-z0-9]{1,16}$', custom_id):
        raise InvalidAPIUsage(INVALID_NAME)
    url_map = URLMap()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(
        {'url': url_map.to_dict()['original'],
         'short_link': url_map.to_dict()['short']}), 201