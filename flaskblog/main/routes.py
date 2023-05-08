from flask import render_template, request, Blueprint, jsonify
from flaskblog.models import Post

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
   page = request.args.get('page', 1, type=int)
   posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=3)
   return render_template('index.html', posts=posts)
   
   # ! JSON DATA
   # posts = Post.query.all()
   # posts_list = [{'title': post.title, 'content': post.content} for post in posts]
   # return jsonify(posts_list)


@main.route('/about')
def about():
   return render_template('about.html', title='About')

@main.route('/sum/<int:n>')
def sum(n):
    if (n>10):
        result = [{
            "id": 3487,
            "value": "greater than 10",
            "state": True
        },
        {
            "id": 3487,
            "value": "greater than 10",
            "state": True
        },[{
            "id": 3487,
            "value": "greater than 10",
            "state": True
        },
        {
            "id": 3487,
            "value": "greater than 10",
            "state": True
        }]
        ]
    else:
        result = {
            "id": 3487,
            "value": "Less than 10",
            "state": False
        }

    return jsonify(result)
