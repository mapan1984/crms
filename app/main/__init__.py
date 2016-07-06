from flask import Blueprint

main = Blueprint('main', __name__) # arg: 蓝本的名字， 蓝本所在的包或模块

# 程序的路由保存在包里的 app/main/views.py 模块中，
# 而错误处理程序保存在 app/main/errors.py 模块中。
# 导入这两个模块就能把路由和错误处理程序与蓝本关联起来。
# 注意，这些模块在 app/main/__init__.py 脚本的末尾导入，
# 这是为了避免循环导入依赖，因为在views.py 和 errors.py 中还要导入蓝本 main 。

from . import views, errors
