from werkzeug.security import generate_password_hash, check_password_hash # 提供密码的散列计算
from flask.ext.login import UserMixin # 提供验证用户方法的默认实现
from . import db, login_manager

import datetime

class Computer(db.Model):
    __tablename__ = 'computers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    start_time = db.Column(db.DateTime)
    spend_time = db.Column(db.Interval)
    # 外键,值为表computers的id,类型为Integer
    # user_id可以为空，表示现在没有用户
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True) 

    def refresh(self):
        if self.start_time is not None:
            self.spend_time = datetime.datetime.now() - self.start_time
        else:
            pass

    def __repr__(self):
        return '<Computer %r>' % self.name

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean)
    # computers属性返回与这个用户相关联的计算机组成的列表
    # 第一个参数Computer表示关联的模型
    # 第二个user向Computer模型中添加一个user属性
    # 这一属性可代替user_id访问User模型，获取模型对象
    computers = db.relationship('Computer', backref='user', lazy='dynamic') 

    @property         # 把password方法变为属性,但读取会引发错误(xxxx = password)
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter  # password的设置(password=xxxxx)
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password): # 根据密码返回真假值
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


# 加载用户的回调函数,使用user_id加载用户,返回特定id的用户对象
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
