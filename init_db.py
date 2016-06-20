#!/usr/bin/env python3
# encoding: utf-8

from hello import db, Role, User

db.drop_all()
db.create_all()

admin_role = Role(name='Admin')
user_role = Role(name='User')

user_mapan = User(username='mapan', password='mapan', role=admin_role)
user_other = User(username='other', password='other', role=user_role)

# 通过db.session管理数据库的改动
db.session.add_all([admin_role, user_role, user_mapan, user_other])
db.session.commit()

print(admin_role.id)

'''
===================================
Python对象 ----> data.sqlite
--------------------------------------
修改行
>>> admin_role.name = 'Administrator'
>>> db.session.add(admin_role)
>>> ad.session.commit()

删除行
>>> db.session.delete(admin_role)
>>> db.session.commit()

查询行
>>> Role.query.all()
[<Role u'Admin'>, <Role u'User'>]

>>> User.query.filter_by(role=user_role).all()
[<User u'other'>]

查看原生SQL查询语句
>>> str(User.query.filter_by(role=user_role))
'SELECT users.id AS users_id, users.username AS users_username,
users.role_id AS users_role_id FROM users WHERE :param_1 = users.role_id'


============================================================
data.sqlite ---------> Python对象
------------------------------------------------
加载名为User的用户角色(在shell中通过数据库查询)
>>> user_role = Role.query.filter_by(name='User').first()
>>> user_role.all()
[<Role 'User'>]


========================================================
Role对象的users属性返回这个对象的
users = db.relationship('User', backref='role') # users属性返回与这个角色相关联的用户组成的列表
--------------------------------------------------------------------------------------
>>> users = user_role.users
>>> users
[<User u'other'>]
>>> users[0].role
<Role u'User'>

添加lazy='dynamic'后，禁止自动查询
>>> user_role.users.order_by(User.username).all()
[<User u'david'>, <User u'susan'>]
>>> user_role.users.count()
2
'''