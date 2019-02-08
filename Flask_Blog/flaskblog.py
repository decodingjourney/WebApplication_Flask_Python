from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask('__name__')

app.config['SECRET_KEY'] = '9c11906fbbcb91a791aa74f616aee41b'

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)