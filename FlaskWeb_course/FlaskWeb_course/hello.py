"""
Examples
"""
import os

from flask import Flask

from flask.ext.script import Manager

from flask import render_template

from flask.ext.bootstrap import Bootstrap

from flask import url_for

from flask.ext.moment import Moment

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required

from flask import session
from flask import redirect

from flask import flash

from flask.ext.sqlalchemy import SQLAlchemy



basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
#db = SQLAlchemy(app)

#bootstrap = Bootstrap(app) # flask-boostrap initilization 

#{::::::::::::::::::::::::::::::    Example 2.1 page 10

#@app.route('/')
#def index():
#    """Renders a sample page."""
#    return '<h1>Hello World!</h1>'


##{::::::::::::::::::::::::::::::    Example 2.2, page 11         this make a dynamic route, took the <name> and put on the web page ()

#@app.route('/user/<name>')
#def user(name):
#    return '<h1>Hello, %s!</h1>' % name




#{::::::::::::::::::::::::::::::    Example page 12             request contexts

#from flask import request
#@app.route('/')
#def index():
#    user_agent = request.headers.get('User-Agent') #variable user_agent
#    return '<p>Your browser is %s</p>' % user_agent


#{::::::::::::::::::::::::::::::    Example page 15             Response

#@app.route('/')
#def index():
#    return '<h1>Bad Request</h1>', 400

#{::::::::::::::::::::::::::::::    Example page 16             Response

#from flask import make_response
#@app.route('/')
#def index():
#    response = make_response('<h1>This document carries a cookie!</h1>')
#    response.set_cookie('answer', '42')
#    return response

#from flask import redirect

#@app.route('/')
#def index():
#    return redirect('http://www.example.com')

#from flask import abort
#@app.route('/user/<id>')
#def get_user(id):
#    user = load_user(id)
#    if not user:
#        abort(404)
#    return '<h1>Hello, %s</h1>' % user.name

#{::::::::::::::::::::::::::::::    Example 2-3  page 17 Use of Flask-script extension


# ...


#if __name__ == '__main__':
#    app.run(debug=True)
#    manager.run()


#{::::::::::::::::::::::::::::::    Example 3-3 Templates


#@app.route('/')
#def index():


#    return render_template('index.html')
 
 
@app.route('/user/<name>')
def user(name):

     return render_template('user.html', name=name)  #store in the argument "name" (placeholder) the variable called "name"



#{::::::::::::::::::::::::::::::    Example 3-6 Template for error handle


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


#{::::::::::::::::::::::::::::::    Example links

#@app.route('/')
#def index():
#    return render_template('index.html')


#{::::::::::::::::::::::::::::::    Example 3-10 favicon

#done on Base

#{::::::::::::::::::::::::::::::    Example 3-11 Flask Moment

#moment = Moment(app)

#{::::::::::::::::::::::::::::::    Example 3-13 Flask Moment

from datetime import datetime

#@app.route('/')
#def index():
#    return render_template('index.html',
#current_time=datetime.utcnow())


#{::::::::::::::::::::::::::::::    Example 4-1 Flask WTF configuration encription Key

app.config['SECRET_KEY'] = 'hard to guess string'

#{::::::::::::::::::::::::::::::    Example 4-1 Flask WTF configuration encription Key

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')


#{::::::::::::::::::::::::::::::    Example 4-4 Flask WTF web forms


#@app.route('/', methods=['GET', 'POST'])
#def index():
#    name = None
#    form = NameForm()
#    if form.validate_on_submit():
#        name = form.name.data
#        form.name.data = ''
    
#    return render_template('index.html', form=form, name=name,
#current_time=datetime.utcnow())


#{::::::::::::::::::::::::::::::    Example 4-4 Flask WTF with redirects and user sesions

#@app.route('/', methods=['GET', 'POST'])
#def index():
#    name = None
#    form = NameForm()
#    if form.validate_on_submit():
#        session['name'] = form.name.data
#        form.name.data = ''
    
#    return render_template('index.html', form=form, name=session.get('name'),
#current_time=datetime.utcnow())


#{::::::::::::::::::::::::::::::    Example 4-4 Flask WTF with redirects and user sesions, GOOD PRACTICE WITH URL_FOR)

#@app.route('/', methods=['GET', 'POST'])
#def index():
#    form = NameForm()
#    if form.validate_on_submit():
#        session['name'] = form.name.data
#        return redirect(url_for('index'))

#    return render_template('index.html', form=form, name=session.get('name'),
#current_time=datetime.utcnow())


#{::::::::::::::::::::::::::::::    Example 4-6 Flashed Messages

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('index'))
    return render_template('index.html',
        form = form, name = session.get('name'), current_time=datetime.utcnow())

#{::::::::::::::::::::::::::::::    Example 5-1 Data base configuration SQLAlchemy

#basedir = os.path.abspath(os.path.dirname(__file__))

#app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] =\
#'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

#db = SQLAlchemy(app)    #The db object instantiated from class SQLAlchemy represents the database and provides
                        #access to all the functionality of Flask-SQLAlchemy

#{::::::::::::::::::::::::::::::    Example 5-2 and 5-3. hello.py: Role and User model definition


#class Role(db.Model):
#   __tablename__ = 'roles'
#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String(64), unique=True)
#   users = db.relationship('User', backref='role', lazy='dynamic')

#   def __repr__(self):
#        return '<Role %r>' % self.name

 

#class User(db.Model):
#    __tablename__ = 'users'
#    id = db.Column(db.Integer, primary_key=True)
#    username = db.Column(db.String(64), unique=True, index=True)
#    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

#    def __repr__(self):
#        return '<User %r>' % self.username


#Step in interactive Python Shell,  create the initial database, import dv object in an interactive Python shell

#from hello import db
#db.create_all()

#Step, To create the database you can use the init_db function:

#from yourapplication.database import init_db
#init_db()




#{::::::::::::::::::::::::::::::    Example 5-3. hello.py: Relationships (only example, up is all the data integrated to the example)

#class Role(db.Model):
#    # ...
#    users = db.relationship('User', backref='role')

#class User(db.Model):
#    # ...
#    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))




#admin_role = Role(name='Admin')
#mod_role = Role(name='Moderator')
#user_role = Role(name='User')
#user_john = User(username='john', role=admin_role)
#user_susan = User(username='susan', role=user_role)
#user_david = User(username='david', role=user_role)

#{::::::::::::::::::::::::::::::  Testing with Flask documentation, SQL Alchemy 


#Testing

from database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()







if __name__ == '__main__':
    app.run(debug=True)
    manager.run()
    