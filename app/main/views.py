from flask import render_template, redirect, request, session, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, \
    current_user
from .. import db
from ..models import User, Computer
from ..email import send_email
from . import main
from .forms import LoginForm, RegistrationForm

import datetime

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
            if user.is_admin:
                login_user(user, form.remember_me.data)
                return redirect(request.args.get('next') or url_for('manage.all_computers'))
            elif not user.is_admin:
                login_user(user, form.remember_me.data)
                if user.computers.first() == None: # 为用户分配电脑
                    free_computer = Computer.query.filter_by(user=None).first()
                    free_computer.user = user
                    free_computer.start_time = datetime.datetime.now()
                    db.session.add(free_computer)
                session['current_user_id']=user.id
                return redirect(request.args.get('next') or url_for('user.information'))
        flash('无效密码')
    return render_template('index.html', form=form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        flash('你现在可以登录了')
        return redirect(url_for('main.index'))
    return render_template('/register.html', form=form)
