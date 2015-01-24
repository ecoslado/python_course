__author__ = 'jesus.pedro.gutierrez.almazan'
import c2.e1_servidor
from flask import Flask
from tools.utils import get_source_lines
from flask.templating import render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

@app.route('/')
def hello_world():
    codigo = get_source_lines(c2.e1_servidor)
    resultado = list()
    results = [(codigo, resultado)]
    return render_template("python_printer.html", template_vars={'results': results})

if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = 'AhLae9chahKua5fuZia7ooji'
    toolbar = DebugToolbarExtension(app)
    app.run(host="0.0.0.0", port=5000)