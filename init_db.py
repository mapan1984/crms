#!/usr/bin/env python3
# encoding: utf-8
import os
import datetime
from app import db
from app.models import User, Computer


db.drop_all()
db.create_all()

admin_mapan = User(email='mapansky1984@163.com', password='mapan', username='马攀', is_admin=True)
user_ben = User(email='1984@sian.com', password='ben', username='王伟', is_admin=False)
user_1ther = User(email='lisi@qq.com', password='lisi', username='李四', is_admin=False)
user_2ther = User(email='zhangwei@qq.com', password='zhangwei', username='张伟', is_admin=False)
user_3ther = User(email='liming@qq.com', password='liming', username='李明', is_admin=False)
user_4ther = User(email='wangyong@qq.com', password='wangyong', username='王勇', is_admin=False)
user_5ther = User(email='zhangjun@qq.com', password='zhangjun', username='张军', is_admin=False)

c1 = Computer(name='c1')
c2 = Computer(name='c2')
c3 = Computer(name='c3')
c4 = Computer(name='c4')
c5 = Computer(name='c5')
c6 = Computer(name='c6')
c1.memo = "序列号：PF035E9C 处理器：AMD A8-6410 APU with AMD Radeon R5 Graphics 2.00GHZ 产品编号：80E1 BIOS: A2CN24WWV1.06 Lenovo G4045 Windows 10 Home China (x64)"
c2.memo = "序列号：PF035E9C 处理器：AMD A8-6410 APU with AMD Radeon R5 Graphics 2.00GHZ 产品编号：80E1 BIOS: A2CN24WWV1.06 Lenovo G4045 Windows 10 Home China (x64)"
c3.memo = "序列号：PF035E9C 处理器：AMD A8-6410 APU with AMD Radeon R5 Graphics 2.00GHZ 产品编号：80E1 BIOS: A2CN24WWV1.06 Lenovo G4045 Windows 10 Home China (x64)"
c4.memo = "序列号：PF035E9C 处理器：AMD A8-6410 APU with AMD Radeon R5 Graphics 2.00GHZ 产品编号：80E1 BIOS: A2CN24WWV1.06 Lenovo G4045 Windows 10 Home China (x64)"
c5.memo = "序列号：PF035E9C 处理器：AMD A8-6410 APU with AMD Radeon R5 Graphics 2.00GHZ 产品编号：80E1 BIOS: A2CN24WWV1.06 Lenovo G4045 Windows 10 Home China (x64)"
c6.memo = "序列号：PF035E9C 处理器：AMD A8-6410 APU with AMD Radeon R5 Graphics 2.00GHZ 产品编号：80E1 BIOS: A2CN24WWV1.06 Lenovo G4045 Windows 10 Home China (x64)"

# 通过db.session管理数据库的改动
db.session.add_all([c1, c2, c3, c4, c5, c6, admin_mapan, user_ben,\
                    user_1ther,user_2ther,user_3ther,user_4ther,user_5ther])
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
