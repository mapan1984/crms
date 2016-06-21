from werkzeug.security import generate_password_hash, check_password_hash # 提供密码的散列计算
from flask.ext.login import UserMixin # 提供验证用户方法的默认实现
from . import db, login_manager

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # users属性返回与这个角色相关联的用户组成的列表
    # 第一个参数User表示关联的模型
    # role向User模型中添加一个role属性
    # 这一属性可代替role_id访问Role模型，获取模型对象
    users = db.relationship('User', backref='role', lazy='dynamic') 

    def __repr__(self):
        return '<Role %r>' % self.name

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # 外键,值为表roles的id,类型为Integer

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


# 加载用户的回掉函数,使用user_id加载用户,返回特定id的用户对象
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
