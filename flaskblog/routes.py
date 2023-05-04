from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required



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
   if current_user.is_authenticated:
      return redirect(url_for('home'))
   form = RegistrationForm()
   if form.validate_on_submit():
      hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
      user = User(username=form.username.data, email=form.email.data, password=hashed_password)
      db.session.add(user)
      db.session.commit()
      flash(f'Your account has been created! You are now able to log in', 'success')
      return redirect(url_for('login'))
   return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
   if current_user.is_authenticated:
      return redirect(url_for('home'))
   form = LoginForm()
   if form.validate_on_submit():
      user = User.query.filter_by(email=form.email.data).first()
      if user and bcrypt.check_password_hash(user.password, form.password.data):
         login_user(user, remember='form.remember.data')
         next_page = request.args.get('next')
         return  redirect(next_page) if next_page else redirect(url_for('home'))
      else:
         flash(f'Invalid Credentials !', 'danger')

   return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
   return render_template('account.html', title='Account')


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