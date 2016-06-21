from flask import render_template, redirect, request, session, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from .. import db
from ..models import User, Role
from ..email import send_email
from . import main
from .forms import LoginForm

'''
由蓝本定义路由: main
定义路由是app为创建，所以使用current_app
url_for使用命名空间
'''
@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.manage'))
        flash('无效密码')
        return redirect(request.args.get('next') or url_for('main.manage'))
    return render_template('index.html', form=form)

@main.route('/manage', methods=['get', 'post'])
def manage():
    return render_template('manage/manage.html', name=session.get('name', 'noname'))

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
