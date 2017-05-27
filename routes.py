import os
import sqlite3
from flask import Flask, render_template, url_for, request
from utils import submit

app = Flask(__name__)

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
