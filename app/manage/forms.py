from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField,\
                    SubmitField, IntegerField, TextAreaField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError

from ..models import Computer


class AddComputerForm(Form):
    name = StringField('电脑编号', validators=[Required(), Length(1, 64)])
    memo = TextAreaField('备忘信息')
    submit = SubmitField('添加')

class DelComputerForm(Form):
    name = StringField('电脑编号', validators=[Required(), Length(1, 64)])
    submit = SubmitField('删除')

class AddUserForm(Form):
    email = StringField('邮件地址', validators=[Required(), Length(1, 64),
                                           Email()])
    username = StringField('用户名', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    password = PasswordField('密码', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('确认密码', validators=[Required()])
    submit = SubmitField('添加')

class DelUserForm(Form):
    name = StringField('用户名', validators=[Required(), Length(1, 64)])
    submit = SubmitField('删除')

class SearchForm(Form):
    name = StringField('电脑编号/用户名',
                       validators=[Required(), Length(1, 64)])
    submit = SubmitField('搜索')

class ChangeForm(Form):
    price = IntegerField('价格', validators=[Required()])
    submit = SubmitField('更改')

class EditProfileForm(Form):
    name = StringField('修改电脑编号', validators=[Length(0, 64)])
    memo = TextAreaField('修改/增加备忘')
    submit = SubmitField('提交')
