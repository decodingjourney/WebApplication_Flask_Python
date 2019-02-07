from flask import Flask, render_template

app = Flask('__name__')

posts = [
    {
        'author': 'Anand Kumar Jha',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'January 7, 2019'
    },
    {
        'author': 'Moti Jha',
        'title': 'Blog Post 2',
        'content': 'second Post content',
        'date_posted': 'January 7, 2019'
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
    app.run()