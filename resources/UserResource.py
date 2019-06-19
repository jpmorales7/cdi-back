import json

import flask
from flask import request, jsonify
from flask_restful import Resource
from models.Models import User, db
from models.Schemas import user_schema
import logging
from resources.ResourceHelper import resource_helper


class Login(Resource):
    def get(self, username, secret_word):
        logging.info('Trying to log user: {}, pass: {}'.format(username, secret_word))
        try:
            user = User.query.filter_by(username=username).first()
            if user is not None and secret_word == user.secretWord:
                logging.info('Login succeed for user: {}'.format(resource_helper.make_dic_user(user)))
                return resource_helper.response(resource_helper.make_dic_user(user), 200)
            msj = 'User: {} not found or password incorrect'.format(username)
            logging.error(msj)
        except Exception as ex:
            logging.error('Error trying to loging: userName {}, msjError: {}'.format(username, ex))
            msj = 'Failed to loging user, error: {}'.format(ex)
        return resource_helper.response(jsonify(message=msj), 400)


class UserResourceClass(Resource):
    def post(self):
        json_data = flask.request.get_json(force=False, silent=True)
        logging.info('Payload: {}'.format(json_data))
        try:
            user, errors = user_schema.load(json_data)
            if errors:
                logging.error(errors)
                raise Exception(errors=errors)
            db.session.add(user)
            db.session.commit()
            msg = 'user: {} was created successfully'.format(user.username)
            logging.info(msg)
            return resource_helper.response(msg, 201)
        except Exception as ex:
            msg_error = 'Error trying to create user, msjError: {}'.format(ex)
            logging.error(msg_error)
            return resource_helper.response(msg_error, 400)



class GetUser(Resource):
    def get(self, username):
        logging.info('Trying to log user: {}'.format(username))
        try:
            user = User.query.filter_by(username=username).first()
            if user is not None:
                logging.info('Login succeed for user: {}'.format(resource_helper.make_dic_user(user)))
                return resource_helper.response(resource_helper.make_dic_user(user), 200)
            msj = 'User: {} not found or password incorrect'.format(username)
            logging.error(msj)
        except Exception as ex:
            logging.error('Error trying to loging: userName {}, msjError: {}'.format(username, ex))
            msj = 'Failed to loging user, error: {}'.format(ex)
        return resource_helper.response(msj, 400)


class ResetPassword(Resource):
    def put(self):
        json_data = request.get_json(force=False, silent=True)
        logging.info('Payload: {}'.format(json_data))
        username = json_data.get("username")
        if username is not None:
            try:
                user = User.query.filter_by(username=username).first()
                if user:
                    if user.username == username and user.secretWord == json_data.get("actualPassword"):
                        user.secretWord = json_data.get("newPassword")
                        db.session.add(user)
                        db.session.commit()
                        return resource_helper.response(jsonify(message='The password was reset for user: {}'.format(username)),
                                             200)
                    error_msj = 'Error checking actualPassword for user: {}'.format(username)
                else:
                    error_msj = 'User nor found, username: {}'.format(username)
            except Exception as ex:
                error_msj = 'Failed trying to update password, userName: {}, msjError: {}'.format(username, ex)
            logging.error(error_msj)
            return resource_helper.response(error_msj, 400)

