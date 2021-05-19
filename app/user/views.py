from flask import render_template, redirect, request, session, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from . import user
from .. import db
from ..models import User


# prefix 为注册路由自动加前缀/user
@user.route('/information/<user_name>', methods=['get', 'post'])
@login_required # flask-login提供的修饰器，保护路由只能由登陆用户访问
def information(user_name):
    current_user = User.query.filter_by(username=user_name).first()
    current_user_computer = current_user.computers.first()
    if current_user_computer is not None:
        current_user_computer.refresh()
        db.session.add(current_user_computer)
    return render_template('user/information.html',
                           user=current_user,
                           user_computer=current_user_computer)

@user.route('/logout')
@login_required
def logout():
    current_user_computer = current_user.computers.first()
    if current_user_computer is not None:
        current_user_computer.user = None   # 退出登录时取消链接电脑
        current_user_computer.start_time = None
    message=''.join(['用户', current_user.username, '现在已经退出'])
    logout_user() # 删除并重折用户回话
    flash(message)
    return redirect(url_for('main.index'))
