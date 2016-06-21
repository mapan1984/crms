from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from . import manage
from ..models import User, Computer
from .forms import AddForm, DelForm

# prefix 为注册路由自动加前缀/manage
@manage.route('/busy_computers')
@login_required  # flask-login提供的修饰器，保护路由只能由登陆用户访问
def busy_computers():
    return render_template('manage/busy_computers.html', 
                           computer_list=Computer.query.all())

@manage.route('/free_computers')
@login_required  # flask-login提供的修饰器，保护路由只能由登陆用户访问
def free_computers():
    return render_template('manage/free_computers.html', 
                           computer_list=Computer.query.all())

@manage.route('/add_del_computers', methods=['GET', 'POST'])
@login_required  # flask-login提供的修饰器，保护路由只能由登陆用户访问
def add_del_computers():
    add_form = AddForm()
    del_form = DelForm()
    return render_template('manage/add_del_computers.html', 
                           computer_list=Computer.query.all(),
                           add_form=add_form, del_form=del_form)

@manage.route('/logout')
@login_required  # flask-login提供的修饰器，保护路由只能由登陆用户访问
def logout():
    logout_user()
    flash('你现在已经退出')
    return redirect(url_for('main.index'))
