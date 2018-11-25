# -*- coding: utf-8 -*-

"""
auth/forms.py

Created on Tue April 10 

@author: rdlc_Dev(alain)
@version:1.180410 

"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
   # remember_me = BooleanField('Se souvenir de moi')
    submit = SubmitField('Valider')

    
