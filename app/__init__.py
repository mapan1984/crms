from flask import Flask
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

mail = Mail()
db = SQLAlchemy()


def create_app(config_name): # 程序的配置名
    app = Flask(__name__)
    app.config.from_object(config[config_name]) # 导入配置
    config[config_name].init_app(app)  # 初始化扩展

    #bootstrap.init_app(app)
    mail.init_app(app)
    #moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)  # 注册蓝本

    return app
