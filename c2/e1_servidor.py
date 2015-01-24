from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

__author__ = 'jesus.pedro.gutierrez.almazan'

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    
    app.debug = True
    app.config['SECRET_KEY'] = 'AhLae9chahKua5fuZia7ooji'
    
    toolbar = DebugToolbarExtension(app)

    app.run(host="0.0.0.0", port=5000)