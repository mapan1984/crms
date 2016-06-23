from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length
from ..models import Computer 


class AddForm(Form):
    name = StringField('电脑编号', validators=[Required(), Length(1, 64)])
    submit = SubmitField('添加')

class DelForm(Form):
    name = StringField('电脑编号', validators=[Required(), Length(1, 64)])
    submit = SubmitField('删除')

class SearchForm(Form):
    name = StringField('电脑编号', validators=[Required(), Length(1, 64)])
    submit = SubmitField('搜索')
