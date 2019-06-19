from flask import Flask
import logging


# def create_app():
#     app = Flask(__name__)
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#                         datefmt='%m-%d %H:%M',
#                         filename='myapp.log',
#                         filemode='w')
#     app.config.from_object('config')
#     console = logging.StreamHandler()
#     formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
#     console.setFormatter(formatter)
#     console.setLevel(logging.INFO)
#
#     logging.getLogger('').addHandler(console)
#     # db = SQLAlchemy(app)
#
#     from app import api_bp
#     app.register_blueprint(api_bp, url_prefix='/api/v1')
#     #ver si se puede hacer mas generico
#     from models.Models import db  # importing db is new
#
#     db.init_app(app)
#
#     return app
#
#
# # def remove_current_session(self, response):
# #     self.Session.remove()
# #     return response
#
# if __name__ == '__main__':
#     app = create_app()
#     app.run(debug=True, port='8001')

