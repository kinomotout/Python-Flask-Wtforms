from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import url_for
from flask import redirect
from flask import flash
from flask_wtf import CSRFProtect

from modelos import db
from modelos import Usuarios
from modelos import Puestos

from configuracion import ConfiguracionDesarrollo

import formularios

import json



app = Flask(__name__)
app.config.from_object(ConfiguracionDesarrollo)

csrf = CSRFProtect()

@app.errorhandler(404)
def pagina_no_encontrada(e):
	return render_template('404.html'), 404

@app.route('/', methods=['GET', 'POST'])
def index():
	formulario_login = formularios.FormularioLogin(request.form)
	if request.method == 'POST' and formulario_login.validate():
		nickUsuario = formulario_login.nick_Usuario.data
		password = formulario_login.password.data


		usuario = Usuarios.query.filter_by(nick_Usuario = nickUsuario).first()

		if usuario is not None and usuario.verificar_password(password):
			mensaje_exito = 'Bienvenido {}'.format(nickUsuario)
			flash(mensaje_exito)
			session['nickUsuario'] = nickUsuario
			return redirect(url_for('inicio'))
		else:
			mensaje_error = 'El password o el usuario es incorrecto'
			flash(mensaje_error)

	return render_template('index.html', titulo1='SGCEI', formulario=formulario_login)

@app.route('/alta_usuario', methods= ['GET', 'POST'])
def altaUsuario():
	puesto2 = Puestos.query.filter_by(id='1').first()
	formulario_alta_usuario = formularios.AltaUsuario(request.form)
	return render_template('altaUsuario.html', titulo1='SGCEI', formulario=formulario_alta_usuario, puesto3 = puesto2.puesto )



if __name__ == '__main__':
	csrf.init_app(app)
	db.init_app(app)

	with app.app_context():
		db.create_all()
	
	app.run(host='192.168.200.58',port=8000)