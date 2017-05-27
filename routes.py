from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/holaheidi')
def holaheidi():
    return render_template('holaheidi.html')

if __name__=='__main__':
    app.run(debug=True)
