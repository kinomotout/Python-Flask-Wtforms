from wtforms import Form
from wtforms import StringField, TextField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from wtforms import HiddenField
from wtforms import PasswordField
from wtforms import SelectField
from modelos import Usuarios


class FormularioLogin(Form):
	nick_Usuario = StringField('Nick de usuario',
		[
			validators.Required(message='El nick del usuario es requerido'),
		]
		)
	password = PasswordField('Password',
		[
			validators.Required(message='El password es requerido')
		]
		)

class AltaUsuario(Form):
	nombre1 = StringField('Primer Nombre')
	nombre2 = StringField('Segundo Nombre')
	apellidoPaterno = StringField('Apellido Paterno')
	apellidoMaterno = StringField('Apellido Materno')
	password = PasswordField('Password')
	email = EmailField('Correo electronico')
	puestoF = SelectField(u'Puestos', coerce=int)

	def puestosField(request):
		puesto1 = puestos.query.get(id)
		formu = AltaUsuario(request.POST, obj=puesto1)
		formu.puestoF.choices = [(g.id, g.puesto) for g in Puestos.query.order_by('id')]


