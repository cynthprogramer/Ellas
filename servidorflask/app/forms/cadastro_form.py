from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    matricula = StringField('Matrícula', validators=[DataRequired()])
    username = StringField('Nome de usuária', validators=[DataRequired(message="Por favor, preencha com um nome de usuária.")])
    senha = PasswordField('Senha', validators=[DataRequired(message="Por favor, preencha com sua senha do SUAP")])