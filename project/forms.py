from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField


class ParameterForm(FlaskForm):
    width = IntegerField('Ширина: ', default=20, name='width')
    height = IntegerField('Высота: ', default=20, name='height')
    submit = SubmitField('Задать размер мира')
