import os

class Configura(object):
	SECRET_KEY = 'Byfab2Q4QFxnPtgyEFKi'

class ConfiguracionDesarrollo(Configura):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/sgcei'
	SQLALCHEMY_TRACK_MODIFICATIONS = False