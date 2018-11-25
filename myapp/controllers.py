# -*- coding: utf-8 -*-

"""
myapp/main/controllers.py

Created on  9|04
           -----
           20|18

@author: rdlc_Dev(alain)
@version:1.0 

"""

from flask import Blueprint

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return "Main"

'''
# Set the route and accepted methods
@auth.route('/signin/', methods=['GET', 'POST'])
def signin():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id

            flash('Welcome %s' % user.name)

            return redirect(url_for('auth.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("auth/signin.html", form=form)
'''
    