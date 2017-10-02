import re
from urllib.parse import unquote

import requests
from flask import Flask, redirect, url_for, request, flash, render_template, make_response
from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from peewee import DoesNotExist

from iselab.models import User
from iselab.settings import SECRET_KEY, WETTY, PROXIES

app = Flask(__name__)
app.secret_key = SECRET_KEY
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def user_loader(user_id):
    return User.get(netid=user_id)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/webshell")
@login_required
def webshell():
    return render_template('term.html', wetty=WETTY)


@app.route("/shell")
def wetty():
    response = make_response()
    user = current_user.netid if current_user.is_authenticated else 'iasg'
    response.headers['X-Accel-Redirect'] = '/wetty/ssh/' + user
    return response


@app.route("/browser")
@login_required
def browser():
    return render_template('browser.html')


def proxify(html, path):
    return re.sub(r"(src=|href=|content=|srcset=|url\()(\"|')(?!http)(?!mailto)(?!\/\/)", r'\1\2{}/'.format(path),
                  html)


@app.route("/browse/")
@login_required
def empty_browse():
    return '', 204


@app.route("/browse/<path:path>", methods=['GET', 'POST'])
@login_required
def browse(path):
    path = unquote(path)
    headers = {'User-Agent': request.headers['User-Agent']}
    if not path.startswith('http'):
        path = 'http://' + path
    if request.method == 'GET':
        r = requests.get(path,
                         proxies=PROXIES,
                         headers=headers,
                         cookies=request.cookies,
                         verify=False)
        return proxify(r.text, path)
    if request.method == 'POST':
        r = requests.post(path,
                          data=request.form.to_dict(flat=True),
                          proxies=PROXIES,
                          headers=headers,
                          cookies=request.cookies,
                          verify=False)
        return proxify(r.text, path)


@app.route("/register")
def register():
    return render_template('term.html', wetty=WETTY, register=True)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = None
    try:
        user = User.get(netid=username)
    except DoesNotExist:
        pass
    if user:
        if user.verify_password(password):
            login_user(user)
            return redirect('/')
    flash('Login failed, try again.')
    return redirect('/')
