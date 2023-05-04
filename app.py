from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config['SECRET_KEY'] = 'ab1c7263106be15a8cd243a10b5ec8cc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(20), unique=True, nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)
   image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
   password = db.Column(db.String(60), nullable=False)
   posts = db.relationship('Post', backref='author', lazy=True)

   def __repr__(self):
      return f"User ('{self.username}', '{self.email}', '{self.image_file}')"
   
class Post(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), nullable=False)
   date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
   content = db.Column(db.Text, nullable=False)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

   def __repr__(self):
      return f"User ('{self.title}', '{self.date_posted}', '{self.content}')"



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



# ? for directly running the file (python manage.py)
# ? if __name__ == '__main__':
# ?   app.run(debug=True)

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