from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import datetime

db = SQLAlchemy()

class Usuarios(db.Model):
	__tablename__= 'usuarios_DB'

	id = db.Column(db.Integer, primary_key=True)
	nick_Usuario = db.Column(db.String(20))
	nombre1 = db.Column(db.String(50))
	nombre2 = db.Column(db.String(50))
	apellido_Paterno = db.Column(db.String(50))
	apellido_Materno = db.Column(db.String(50))
	password = db.Column(db.String(66))
	email = db.Column(db.String(40))
	envio_Email = db.Column(db.Integer)
	puesto = db.Column(db.Integer)

	estatus = db.Column(db.Integer)

	def __init__(self, nick_Usuario, nombre1, nombre2, apellido_Paterno, apellido_Materno,
					password, email, envio_Email, puestoF, estatus):
		self.nick_Usuario = nick_Usuario
		self.nombre1 = nombre1
		self.nombre2 = nombre2
		self.apellido_Paterno = apellido_Paterno
		self.apellido_Materno = apellido_Materno
		self.password = password
		self.email = email
		self.envio_Email = envio_Email
		self.puestoF = puestoF
		self.estatus = estatus


	def __crear_password(self, password):
		return generate_password_hash(self.password, password)

	def verificar_password(self, password):
		return check_password_hash(self.password, password)


class Puestos(db.Model):
	__tablename__= 'puestos'

	id = db.Column(db.Integer, primary_key=True)
	puesto = db.Column(db.String(50))

	def __init__(self, nombre_Puesto):
		self.nombre_Puesto = nombre_Puesto

