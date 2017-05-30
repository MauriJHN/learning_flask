import os
from flask import Flask, render_template, url_for, request, redirect, url_for
from models import db, User
from forms import SignupForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_NAME'] = 'postgresql://localhost/learningflask'
# secret key that enables wtf to generate secure forms
app.secret_key = 'development-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/pa')
def papa():
    return render_template('papa.html')

@app.route('/log', methods=['POST'])
def create():
    objects = request.form

    return '<h1>All is well</h1>'

@app.route('/test')
def test():
    return render_template('input_test.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if request.method == 'POST':
        # check if the data entered is valid
        if form.validate() == False:
            return render_template('signup.html', form=form)
        else:

            new_user = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
            db.session.add(new_user)
            db.session.commit()

            # session contains a cookie with the user id
            session['email'] = new_user.email
            # redirect to the homepage
            return redirect(url_for('home'))
    elif request.method == 'GET':
        return render_template('signup.html', form=form)

@app.route('/home')
def home():
    return render_template('home')

# snippet: enables stylesheet update
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)
# end of snippet


if __name__=='__main__':
    app.run(debug=True)
