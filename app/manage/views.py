from flask import render_template, redirect, request, session, url_for, flash, abort
from flask.ext.login import login_user, logout_user, login_required, current_user
from . import manage
from .forms import AddComputerForm, DelComputerForm, AddUserForm,\
                  DelUserForm, SearchForm, EditProfileForm
from .. import db
from ..models import User, Computer

import functools

def all_computers_refresh(func): # 定义装饰器，动态更新所有电脑信息
    @functools.wraps(func)
    def wrapper(*args, **kw):
        computer_list = Computer.query.all()
        for computer in computer_list:
            computer.refresh()
            db.session.add(computer)
        return func(*args, **kw)
    return wrapper

# prefix 为注册路由自动加前缀/manage
@manage.route('/all_computers', methods=['GET', 'POST'])
@login_required
@all_computers_refresh
def all_computers():
    return render_template('manage/all_computers.html', 
                           computer_list=Computer.query.all(),
                           search_form=SearchForm())

@manage.route('/busy_computers')
@login_required
@all_computers_refresh
def busy_computers():
    return render_template('manage/busy_computers.html', 
                           computer_list=Computer.query.all(),
                           search_form=SearchForm())

@manage.route('/free_computers')
@login_required
@all_computers_refresh
def free_computers():
    return render_template('manage/free_computers.html', 
                           computer_list=Computer.query.all(),
                           search_form=SearchForm())

@manage.route('/add_computers', methods=['get', 'post'])
@login_required
@all_computers_refresh
def add_computers():
    add_form = AddComputerForm()
    if add_form.validate_on_submit():
        computer = Computer.query.filter_by(name=add_form.name.data).first()
        if computer == None:
            c = Computer(name=add_form.name.data, memo=add_form.memo.data)
            db.session.add(c)
            flash('添加成功，电脑已添加')
        else:
            flash('添加失败，电脑已存在')
        return redirect(url_for('manage.add_computers'))
    return render_template('manage/add_computers.html', 
                           computer_list=Computer.query.all(),
                           search_form=SearchForm(),
                           add_form=add_form)

@manage.route('/del_computers', methods=['GET', 'POST'])
@login_required
@all_computers_refresh
def del_computers():
    del_form = DelComputerForm()
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
                           search_form=SearchForm(),
                           del_form=del_form)

@manage.route('/all_users')
@login_required
@all_computers_refresh
def all_users():
    return render_template('manage/all_users.html', 
                           search_form=SearchForm(),
                           user_list=User.query.all())

@manage.route('/busy_users')
@login_required
@all_computers_refresh
def busy_users():
    return render_template('manage/busy_users.html', 
                           search_form=SearchForm(),
                           user_list=User.query.all())

@manage.route('/free_users')
@login_required
@all_computers_refresh
def free_users():
    return render_template('manage/free_users.html', 
                           search_form=SearchForm(),
                           user_list=User.query.all())

@manage.route('/add_users', methods=['get', 'post'])
@login_required
@all_computers_refresh
def add_users():
    add_form = AddUserForm()
    if add_form.validate_on_submit():
        user = User.query.filter_by(username=add_form.username.data).first()
        if user == None:
            u = User(username=add_form.username.data, email=add_form.email.data, 
                     password=add_form.password.data)
            db.session.add(u)
            flash('添加成功，用户已添加')
        else:
            flash('添加失败，用户已存在')
        return redirect(url_for('manage.add_users'))
    return render_template('manage/add_users.html', 
                           user_list=User.query.all(),
                           search_form=SearchForm(),
                           add_form=add_form)

@manage.route('/del_users', methods=['GET', 'POST'])
@login_required
@all_computers_refresh
def del_users():
    del_form = DelUserForm()
    if del_form.validate_on_submit():
        user = User.query.filter_by(username=del_form.name.data).first()
        if user != None:
            db.session.delete(user)
            flash('删除成功，用户已删除')
        else:
            flash('删除失败，用户不存在')
        return redirect(url_for('manage.del_users'))
    return render_template('manage/del_users.html', 
                           user_list=User.query.all(),
                           search_form=SearchForm(),
                           del_form=del_form)

@manage.route('/search_computer', methods=['POST'])
@login_required
@all_computers_refresh
def search_computer():
    search_form = SearchForm()
    computer = Computer.query.filter_by(name=search_form.name.data).first()
    user = User.query.filter_by(username=search_form.name.data).first()
    if computer is not None:
        return redirect(url_for('manage.computer', computer_name=computer.name))
    elif user is not None:
        return redirect(url_for('user.information', user_name=user.username))
    else:
        abort(404)

@manage.route('/computer/<computer_name>', methods=['GET', 'POST'])
@login_required
@all_computers_refresh
def computer(computer_name):
    edit_profile_form = EditProfileForm()
    computer = Computer.query.filter_by(name=computer_name).first()
    if computer is None:
        abort(404)
    if edit_profile_form.validate_on_submit():
        computer.name = edit_profile_form.name.data
        computer.memo = edit_profile_form.memo.data
        db.session.add(computer)
        flash('电脑信息已更新')
        return redirect(url_for('manage.computer', computer_name=computer.name))
    edit_profile_form.name.data = computer.name
    edit_profile_form.memo.data = computer.memo
    return render_template('manage/computer.html', computer=computer,
                           search_form=SearchForm(), edit_profile_form=edit_profile_form)

@manage.route('/logout')
@login_required  # flask-login提供的修饰器，保护路由只能由登陆用户访问
def logout():
    logout_user()
    flash('管理员mapan现在已经退出')
    return redirect(url_for('main.index'))
