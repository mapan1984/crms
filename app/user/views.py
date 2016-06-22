from flask import render_template, redirect, request, session, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from . import user
from ..models import User


# prefix 为注册路由自动加前缀/user
@user.route('/user', methods=['get', 'post'])
def information():
    current_user = User.query.filter_by(id=session.get('current_user_id')).first()
    current_user_computer = current_user.computers.first()
    return render_template('user/information.html', 
                           user=current_user,
                           user_computer=current_user_computer)

@user.route('/logout')
@login_required  # flask-login提供的修饰器，保护路由只能由登陆用户访问
def logout():
    current_user = User.query.filter_by(id=session.get('current_user_id')).first()
    message=''.join(['用户', current_user.username, '现在已经退出'])
    logout_user() # 删除并重折用户回话
    flash(message)
    return redirect(url_for('main.index'))
