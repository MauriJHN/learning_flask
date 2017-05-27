from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

<<<<<<< HEAD
@app.route('/about')
def about():
    return render_template('about.html')
=======
@app.route('/holaheidi')
def holaheidi():
    return render_template('holaheidi.html')
>>>>>>> e2561812c64c516e0daeb1dcac81234320429ad4

if __name__=='__main__':
    app.run(debug=True)
