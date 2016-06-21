from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from . import auth
from ..models import User


# prefix 为注册路由自动加前缀/auth
@auth.route('/logout')
#@login_required
def logout():
    #logout_user()
    flash('已经退出')
    return redirect(url_for('main.index'))
