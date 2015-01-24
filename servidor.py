# -*- coding: utf-8 -*-
__author__ = 'jesus.pedro.gutierrez.almazan'
from flask import Flask
from c2 import e1_servidor
from tools.utils import get_source_lines
from c4 import e1_flujo, e2_flujo, e3_flujo
from flask.templating import render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

@app.route('/')
def hello_world():
    codigo = get_source_lines(e1_servidor)
    resultado = list()
    results = [(codigo, resultado)]
    return render_template("c2_servidor.html", template_vars={'results': results})

@app.route('/c4/e1')
def c4_e1_flujo():
    codigo = get_source_lines(e1_flujo)
    resultado = list()
    results = [(codigo, resultado)]
    return render_template("c2_servidor.html", template_vars={'results': results})

@app.route('/c4/e2')
def c4_e2_flujo():
    codigo = get_source_lines(e2_flujo)
    resultado = list()
    results = [(codigo, resultado)]
    return render_template("c2_servidor.html", template_vars={'results': results})

@app.route('/c4/e3')
def c4_3_flujo():
    codigo = get_source_lines(e3_flujo)
    resultado = list()
    results = [(codigo, resultado)]
    return render_template("c2_servidor.html", template_vars={'results': results})


if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = 'AhLae9chahKua5fuZia7ooji'
    toolbar = DebugToolbarExtension(app)
    app.run(host="0.0.0.0", port=5000)