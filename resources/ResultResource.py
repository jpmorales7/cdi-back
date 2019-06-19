import logging

import flask
import numpy as np
from flask_restful import Resource
from sqlalchemy import func

from models.Schemas import *
from models.Models import Results
from resources.ResourceHelper import resource_helper

ages = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


class ResultsResource(Resource):
    def get(self, gender):
        logging.info('Getting results for: {}'.format(gender))
        result_dict = []
        try:
            for i in ages:
                result_list = self.get_result_list(gender, i)
                dict_aux = {
                    "age": i,
                    "10": np.percentile(result_list, 10),
                    "25": np.percentile(result_list, 25),
                    "50": np.percentile(result_list, 50),
                    "75": np.percentile(result_list, 75),
                    "90": np.percentile(result_list, 90)}
                result_dict.append(dict_aux)
                logging.info('Percentile {} : {}'.format(i, dict_aux))
            return resource_helper.response(result_dict, 200)
        except Exception as ex:
            msg_error = 'Getting results for: {}, error {}'.format(gender, ex)
            logging.error(msg_error)
        return resource_helper.response(msg_error, 400)

    def get_result_list(self, gender, i):
        result_list = None
        if gender == 'all':
            result_list = db.session.query(Results.result).filter(Results.age == i).all()
        else:
            if gender == 'feminine':
                result_list = db.session.query(Results.result).filter(
                    Results.age == i and Results.gender == 'femenine').all()
            if gender == 'masculine':
                result_list = db.session.query(Results.result).filter(
                    Results.age == i and Results.gender == 'masculine').all()
        return result_list


class ResultsParents(Resource):
    def get(self, user):
        logging.info('Getting results for: {}'.format(user))

        try:
            children = Children.query.filter_by(userId=user).first()
            survey = Survey.query.filter_by(childrenId=children.id).first()
            count = db.session.query(Results.result).filter(
                Results.age == survey.age and Results.result <= survey.results).count()
            count_total = db.session.query(Results.result).filter(Results.age == survey.age).count()
            percentile = (count - 0.5) / count_total * 100
            if percentile < 10:

                min = 0
                max = 10
            else:
                if percentile < 25:
                    min = 10
                    max = 25
                else:
                    if percentile < 50:
                        min = 25
                        max = 50
                    else:
                        if percentile < 75:
                            min = 50
                            max = 75
                        else:
                            if percentile < 90:
                                min = 75
                                max = 90
                            else:
                                min = 90
                                max = 100

            message = "Su hija/o se encuentra entre el {}% y {}% de la poblacion de su edad".format(min, max)
            return resource_helper.response(message, 200)
        except Exception as ex:
            msg_error = 'Error trying to getting results,  msjError: {}'.format(ex)
            logging.error(msg_error)
            return resource_helper.response(msg_error, 400)
