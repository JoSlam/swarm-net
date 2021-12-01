from flask import Blueprint, jsonify, request
from flask_jwt import jwt_required

topic_views = Blueprint('topic_views', __name__, template_folder='../templates')

from App.controllers.topic import (
    edit_topic,
    get_popular_topics,
    get_topics,
    create_topic,
    get_topic_by_id,
    delete_topic_by_id,
)

# Get all topics
@topic_views.route('/topics', methods=["GET"])
@jwt_required()
def get_all_topics():
    filter_popular = request.args.get('popular')

    if filter_popular:
        topics = get_popular_topics()
    else:
        topics = get_topics()
    return jsonify(topics)

# create Topic
@topic_views.route('/topics', methods=["POST"])
@jwt_required()
def create_new_topic():
    text = request.json.get('text')
    level = request.json.get('level')
    topic = create_topic(text, level)
    return jsonify(topic)


# edit Topic
@topic_views.route('/topics/<int:topic_id>', methods=["PUT"])
@jwt_required()
def update_topic(topic_id):
    text = request.json.get('text')
    level = request.json.get('level')
    
    topic = edit_topic(topic_id, text, level)
    if topic:
        return jsonify(topic)
    else: 
        return 404


# get specific Topic by ID
@topic_views.route('/topics/<int:topic_id>', methods=["GET"])
def get_topic(topic_id):
    topic = get_topic_by_id(topic_id)
    return jsonify(topic.toDict())

#Deletes topic from database and returns if it was successful
@topic_views.route('/topics/<int:topic_id>', methods=["DELETE"])
def delete_topic(topic_id):
    result = delete_topic_by_id(topic_id)
    if result:
        return jsonify(result)
    else:
        return 404