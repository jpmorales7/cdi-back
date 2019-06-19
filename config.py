import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI= 'mysql+pymysql://proyectocdicdi:adminadmin@db4free.net:3306/proyectocdicdi'