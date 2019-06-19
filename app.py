from flask import Blueprint
from flask_restful import Api
from flask import Flask
import logging

from resources.ChildrenResource import CreateChildren, GetChildren
from resources.ImportResource import ImportData
from resources.ResultResource import ResultsParents
from resources.SurveyResource import CreateSurvey, UpdateSurvey, SurveyResource
from resources.UserResource import Login, ResetPassword, UserResourceClass, GetUser
from resources.ResultResource import ResultsResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route

api.add_resource(ResetPassword, '/user/resetPassword')
api.add_resource(UserResourceClass, '/user/create')
api.add_resource(GetUser, '/user/<string:username>')

api.add_resource(Login, '/authorize/<string:username>/<string:secret_word>')

#Children

api.add_resource(CreateChildren, '/children/create/<string:user>')
api.add_resource(GetChildren, '/children/get/<string:user_id>')


#Survey
api.add_resource(CreateSurvey, '/survey/create/<string:user>')
api.add_resource(UpdateSurvey, '/survey/update/<string:table>/<string:user>')
api.add_resource(SurveyResource, '/survey/get/<string:user>')


#Results
api.add_resource(ResultsParents, '/resultParents/<string:user>')
api.add_resource(ResultsResource, '/results/<string:gender>')

#Import
api.add_resource(ImportData, '/import')


def create_app():
    app = Flask(__name__)
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='myapp.log',
                        filemode='w')
    app.config.from_object('config')
    console = logging.StreamHandler()
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    console.setLevel(logging.INFO)

    logging.getLogger('').addHandler(console)
    # db = SQLAlchemy(app)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')
    # ver si se puede hacer mas generico
    from models.Models import db  # importing db is new

    db.init_app(app)

    return app


# def remove_current_session(self, response):
#     self.Session.remove()
#     return response

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
