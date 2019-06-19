import json
import logging

import flask
from flask import make_response, Response
from flask.json import jsonify
from flask_restful import Resource

from models.Schemas import children_schema

from models.Models import Children
from models.Models import db

from resources.ResourceHelper import resource_helper


class CreateChildren(Resource):
    def __init__(self):
        Resource.__init__(self)
        self.children_schema = children_schema

    def post(self, user):
        json_data = flask.request.get_json(force=False, silent=True)
        logging.info('Payload: {}'.format(json_data))
        try:
            #   address = address_schema.load(json_data.address)
            children, errors = children_schema.load(json_data)
            if errors:
                logging.error(errors)
                raise Exception(errors=errors)
            children.userId = user
            db.session.add(children)
            db.session.commit()
            msg = 'Children: {} was created successfully'.format(children.id)
            logging.info(msg)
            return resource_helper.response(msg, 201)
        except Exception as ex:
            msg_error = 'Error trying to create children, msjError: {}'.format(ex)
            logging.error(msg_error)
            return resource_helper.response(msg_error, 400)


class GetChildren(Resource):
    def get(self, user_id):
        logging.info('Trying to get children from user: {}'.format(user_id))
        try:
            children = Children.query.filter_by(userId=user_id).first()
            if children is not None:
                logging.info('Login succeed for user: {}'.format(children))
                return resource_helper.response(resource_helper.make_dic_children(children), 200)
            msj = 'Children for user: {} not found '.format(user_id)
            logging.error(msj)
        except Exception as ex:
            logging.error('Error getting child {}, msjError: {}'.format(user_id, ex))
            msj = 'Failed to create user, error: {}'.format(ex)
        return resource_helper.response(msj, 400)

