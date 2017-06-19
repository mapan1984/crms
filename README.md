## 使用

本系统使用Flask框架进行开发，可以按以下步骤使用：

1. 安装Python 3, 用以提供Python 3脚本运行环境;
2. 进入程序目录，运行以下命令,安装扩展;

        $ pip install -r requirements.txt

4. 设置环境变量`ADMIN_EMAIL`为管理员邮件地址，`MAIL_USERNAME`、`MAIL_PASSWORD`为代理邮件地址和密码;
3. 进入程序目录，运行以下命令,开启服务器;

        $ python manage.py runserver

4. 在浏览器中访问: `http://127.0.0.1:5000`，即可访问机房管理系统首页，进行后续操作。
