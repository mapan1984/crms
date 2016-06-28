from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Required, Length
from ..models import Computer 


class AddComputerForm(Form):
    name = StringField('电脑编号', validators=[Required(), Length(1, 64)])
    memo = TextAreaField('备忘信息')
    submit = SubmitField('添加')

class DelComputerForm(Form):
    name = StringField('电脑编号', validators=[Required(), Length(1, 64)])
    submit = SubmitField('删除')

class AddUserForm(Form):
    name = StringField('用户名', validators=[Required(), Length(1, 64)])
    submit = SubmitField('添加')

class DelUserForm(Form):
    name = StringField('用户名', validators=[Required(), Length(1, 64)])
    submit = SubmitField('删除')

class SearchForm(Form):
    name = StringField('电脑编号', validators=[Required(), Length(1, 64)])
    submit = SubmitField('搜索')

class EditProfileForm(Form):
    name = StringField('修改电脑编号', validators=[Length(0, 64)])
    memo = TextAreaField('修改/增加备忘')
    submit = SubmitField('提交')
