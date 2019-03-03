# -*- coding: utf-8 -*-

"""
auth/forms.py

Created on Tue April 10 

@author: rdlc_Dev(alain)
@version:1.180410 

"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    """Login form to access admin pages"""

    username = StringField('Utilisateur', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    useremail = StringField('Courriel', validators=[DataRequired()])
