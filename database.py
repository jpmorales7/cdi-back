from flask_sqlalchemy import SQLAlchemy



def init_db():
    global db
    db = SQLAlchemy()
