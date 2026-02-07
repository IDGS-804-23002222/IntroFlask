from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField, SubmitField
from wtforms.validators import DataRequired, NumberRange, InputRequired, ValidationError

class CinepolisForm(FlaskForm):
    nombre = StringField(
        'Nombre',
        validators=[InputRequired(message="El nombre es obligatorio")]
    )

    compradores = IntegerField(
        'Cantidad de compradores',
        validators=[
            InputRequired(message="La cantidad de compradores es obligatoria"),
            NumberRange(min=1, message="Debe haber al menos 1 comprador")
        ]
    )

    boletos = IntegerField(
        'Cantidad de boletos',
        validators=[
            InputRequired(message="La cantidad de boletos es obligatoria"),
            NumberRange(min=1, message="Debe comprar al menos 1 boleto")
        ]
    )

    tarjeta = RadioField(
        'Tarjeta CINECO',
        choices=[('si', 'Sí'), ('no', 'No')],
        default='no'
    )
    
    def validate_boletos(self, field):
        if self.compradores.data is not None:
            max_boletos = self.compradores.data * 7
            if field.data > max_boletos:
                raise ValidationError(
                    f"Solo se pueden comprar {max_boletos} boletos "
                )

    submit = SubmitField('Procesar')
