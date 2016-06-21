from flask import render_template, session, redirect, url_for, current_app

from .. import db
from ..models import User, Role
from ..email import send_email
from . import main
from .forms import NameForm

'''
由蓝本定义路由: main
定义路由是app为创建，所以使用current_app
url_for使用命名空间
'''
@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None: # 用户第一次登陆
            user_role = Role.query.filter_by(name='User').first()
            user = User(username=form.name.data, password=form.password.data, role=user_role)
            db.session.add(user)
            session['known'] = False
            if current_app.config['BEN_ADMIN']:
                send_email(current_app.config['BEN_ADMIN'], 'New User',
                           'mail/new_user', user=user)
        else: #用户不是第一次登陆
            session['known'] = True
        session['name'] = form.name.data
        form.name.date = ''
        session['password'] = form.password.data
        return redirect(url_for('main.manage'))
    return render_template('index.html', form=form)


@main.route('/manage', methods=['get', 'post'])
def manage():
    return render_template('manage.html', name=session.get('name'), 
                           known=session.get('known'))


@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)
