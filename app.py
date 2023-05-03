from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'ab1c7263106be15a8cd243a10b5ec8cc'

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
   return render_template('home.html', posts=posts)

@app.route('/about')
def about():
   return render_template('about.html', title='About')


# ? form routes
@app.route('/register')
def register():
   form = RegistrationForm()
   return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
   form = LoginForm()
   return render_template('login.html', title='About', form=form)



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