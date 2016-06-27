#!/usr/bin/env python3
# encoding: utf-8
import os
import datetime
from app import db
from app.models import User, Computer


db.drop_all()
db.create_all()

admin_mapan = User(email='mapansky1984@163.com', username='mapan', is_admin=True)
admin_mapan.password = 'mapan'
user_other = User(email='2642896890@qq.com', username='other', is_admin=False)
user_other.password = 'other'

c1 = Computer(name='c1')
c2 = Computer(name='c2')
c3 = Computer(name='c3')
c4 = Computer(name='c4')
c5 = Computer(name='c5')
c6 = Computer(name='c6')
c1.memo = "i an c1, lalala , i am the best computer"

# 通过db.session管理数据库的改动
db.session.add_all([c1, c2, c3, c4, c5, c6, admin_mapan, user_other])
db.session.commit()

print(c1.id)


f=True

def test_time():
    global f
    c=Computer.query.filter_by(name='c1').first()
    if f:
        c.start_time = datetime.datetime.now()
        i=False
    else:
        print(c.current_time)
        print(c.spend_time)
