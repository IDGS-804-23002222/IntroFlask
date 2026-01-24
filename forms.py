from wtforms import Form
from wtforms import StringField, PasswordField, EmailField, BooleanField, IntegerField

#validators para validar los campos
from wtforms import validators


class userForm(Form):
    matricula=IntegerField("Matricula", [
        validators.DataRequired(message='El campo es requerido')
    ])
    nombre=StringField("Nombre", [
        validators.DataRequired(message='El campo es requerido')
    ])
    apellido=StringField("Apellido", [
        validators.DataRequired(message='El campo es requerido')
    ])
    correo=EmailField("Correo", [
        validators.Email(message='Ingrese correo valido')
    ])
    