from wtforms import Form
from wtforms import StringField
from wtforms import TextField
from wtforms import PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField
from wtforms import validators

def length_honeypot(form, field):
	if len(field.data) > 0:
		raise validators.ValidationError('El campo debe estar vacío.')

class CommentForm(Form):
	username = StringField('Username',
				[ 
					validators.Required(message='El username es requerido!'),
					validators.length(min=4, max=25, message='Ingrese un username valido!')
				])
	email = EmailField('Correo electronico',
				[
					validators.Required(message='El username es requerido!'),
					validators.Email(message='Ingrese un email valido!')
				])
	comment = TextField('Comentario')
	honeypot = HiddenField('', [length_honeypot])

class LoginForm(Form):
	username = StringField('Username',
				[
					validators.Required(message = 'El Username es requerido!'),
					validators.length(min=8, max=8, message='Ingrese un Username de 8 caracteres!'),
				])
	password = PasswordField('Password', [validators.Required(message='Ingrese el password.')])
	