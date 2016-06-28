from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.moment import Moment
from flask.ext.login import LoginManager
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()

# 初始化 flask-login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'index.login'  # 注册蓝本的登陆页面路由

def create_app(config_name): # 程序的配置名
    app = Flask(__name__) # 传递__name__值，确定根目录，定位资源文件
    app.config.from_object(config[config_name]) # 导入配置
    config[config_name].init_app(app)  # 初始化扩展

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)  # 注册蓝本

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint, url_prefix='/user')  # prefix会使注册为/login
                                                                # 的路由变为/auth/login
    from .manage import manage as manage_blueprint
    app.register_blueprint(manage_blueprint, url_prefix='/manage')

    return app
