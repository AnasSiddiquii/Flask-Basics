from flask import Flask, render_template, url_for
app = Flask(__name__)

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

@app.route('/')
@app.route('/home')
def home():
   return render_template('home.html', posts=posts)

@app.route('/about')
def about():
   return render_template('about.html', title='About')



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