from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField #字段对象
from wtforms.validators import Required      #验证函数

class NameForm(Form):
    name = StringField('用户名', validators=[Required()])         # type="text"的<input>
    password = PasswordField('输入密码', validators=[Required()]) # type="password的<input>"
    submit = SubmitField('登陆')                                  # type="submit"的<input>
