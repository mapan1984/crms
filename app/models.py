from . import db

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

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id')) # 外键,值为表roles的id,类型为Integer

    def __repr__(self):
        return '<User %r>' % self.username
