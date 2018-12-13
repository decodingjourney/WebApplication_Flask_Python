from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b1b794927704b4caa3a0e1fcac64c6c0'

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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {{ form.username.data }}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)



@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)
