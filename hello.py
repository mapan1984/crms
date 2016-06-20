from flask import Flask, render_template, session, redirect, url_for
from flask.ext.script import Manager

# {{{ wtf
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField #字段对象
from wtforms.validators import Required      #验证函数
# end_wtf}}}


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

manager = Manager(app)


class NameForm(Form):
    name = StringField('用户名', validators=[Required()])         # type="text"的<input>
    password = PasswordField('输入密码', validators=[Required()]) # type="password的<input>"
    submit = SubmitField('登陆')                                  # type="submit"的<input>


@app.route('/', methods=['get', 'post'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['password'] = form.password.data
        return redirect(url_for('manage'))
    return render_template('index.html', form=form, name=session.get('name'))


@app.route('/manage', methods=['get', 'post'])
def manage():
    return render_template('manage.html', name=session.get('name'))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    manager.run()
