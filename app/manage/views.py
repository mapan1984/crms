from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from .. import db
from . import manage
from ..models import User, Computer
from .forms import AddForm, DelForm

# prefix 为注册路由自动加前缀/manage
@manage.route('/all_computers')
@login_required
def all_computers():
    return render_template('manage/all_computers.html', computer_list=Computer.query.all())

@manage.route('/busy_computers')
@login_required
def busy_computers():
    return render_template('manage/busy_computers.html', 
                           computer_list=Computer.query.all())

@manage.route('/free_computers')
@login_required
def free_computers():
    return render_template('manage/free_computers.html', 
                           computer_list=Computer.query.all())

@manage.route('/add_computers', methods=['GET', 'POST'])
@login_required
def add_computers():
    add_form = AddForm()
    if add_form.validate_on_submit():
        computer = Computer.query.filter_by(name=add_form.name.data).first()
        if computer == None:
            c = Computer(name=add_form.name.data)
            db.session.add(c)
            flash('添加成功，电脑已添加')
        else:
            flash('添加失败，电脑已存在')
        return redirect(url_for('manage.add_computers'))
    return render_template('manage/add_computers.html', 
                           computer_list=Computer.query.all(),
                           add_form=add_form)

@manage.route('/del_computers', methods=['GET', 'POST'])
@login_required
def del_computers():
    del_form = DelForm()
    if del_form.validate_on_submit():
        computer = Computer.query.filter_by(name=del_form.name.data).first()
        if computer != None:
            db.session.delete(computer)
            flash('删除成功，电脑已删除')
        else:
            flash('删除失败，电脑不存在')
        return redirect(url_for('manage.del_computers'))
    return render_template('manage/del_computers.html', 
                           computer_list=Computer.query.all(),
                           del_form=del_form)

@manage.route('/all_users')
@login_required
def all_users():
    return render_template('manage/all_users.html', 
                           user_list=User.query.all())

@manage.route('/logout')
@login_required  # flask-login提供的修饰器，保护路由只能由登陆用户访问
def logout():
    logout_user()
    flash('管理员mapan现在已经退出')
    return redirect(url_for('main.index'))
