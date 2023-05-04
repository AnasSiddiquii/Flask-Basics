from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
   {
      'title': 'Post-1',
      'name': 'Anas',
      'content': 'Hello World',
      'date': '2020-01-01'
   },
   {
      'title': 'Post-2',
      'name': 'Saif',
      'content': 'Hi World',
      'date': '2022-03-08'
   }
]


# ? simple routes
@app.route('/')
@app.route('/home')
def home():
   return render_template('index.html', posts=posts)

@app.route('/about')
def about():
   return render_template('about.html', title='About')


# ? form routes
@app.route('/register', methods=['GET', 'POST'])
def register():
   form = RegistrationForm()
   if form.validate_on_submit():
      flash(f'Account created of {form.username.data} !', 'success')
      return redirect(url_for('home'))
   return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
   form = LoginForm()
   if form.validate_on_submit():
      if form.email.data == 'a@gmail.com' and form.password.data == 'pass':
         flash(f'Login Successful !', 'success')
         return redirect(url_for('home'))
      else:
         flash(f'Invalid Credentials !', 'danger')

   return render_template('login.html', title='Login', form=form)


# ? html homepage
# @app.route('/')     # ? opens the same route
# @app.route('/home') # ? opens the same route
# def home():
#    return '''
#    <!doctype html>
#    <html>
#       <head>
#          <title>Home</title>
#       </head>
#       <body>
#          <h1>Home</h1>
#       </body>
#    </html>
#    '''

# ? html aboutpage
# @app.route('/about')
# def about():
#    return '<center><h1>About Page<h1/></center>'