from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Anand jha',
        'title': 'Blog Post 1',
        'content': 'First Blog Post',
        'date_posted': 'December 12, 2018'
    },
    {
        'author': 'Sonam jha',
        'title': 'Blog Post 2',
        'content': 'second Blog Post',
        'date_posted': 'December 11, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
