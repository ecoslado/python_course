# -*- coding: utf-8 -*-
__author__ = 'jesus.pedro.gutierrez.almazan'

from c2 import e1_servidor

from tools.utils import get_source_lines, get_file_contents

from flask import Flask
from flask.templating import render_template
from flask_debugtoolbar import DebugToolbarExtension

from importlib import import_module

app = Flask(__name__)

@app.route('/')
def hello_world():
    codigo = get_source_lines(e1_servidor)
    resultado = list()
    results = [(codigo, resultado)]
    return render_template("c2_servidor.html", template_vars={'results': results})

@app.route('/flujo/if')
def c4_e1_flujo_if():
    codigo = get_file_contents('./python_course/c4/e1_flujo_if.txt')
    resultado = list()
    results = [(codigo, resultado)]
    return render_template("c2_servidor.html", template_vars={'results': results})

@app.route('/flujo/for')
def c4_e1_flujo_for():
    codigo = get_file_contents('./python_course/c4/e1_flujo_for.txt')
    resultado = list()
    results = [(codigo, resultado)]
    return render_template("c2_servidor.html", template_vars={'results': results})

@app.route('/flujo/range')
def c4_e1_flujo_range():
    codigo = get_file_contents('./python_course/c4/e1_flujo_range.txt')
    resultado = list()
    results = [(codigo, resultado)]
    return render_template("c2_servidor.html", template_vars={'results': results})

@app.route('/flujo/while')
def c4_e1_flujo_while():
    codigo = get_file_contents('./python_course/c4/e1_flujo_while.txt')
    resultado = list()
    results = [(codigo, resultado)]
    return render_template("c2_servidor.html", template_vars={'results': results})

@app.route('/flujo/comprehension')
def c4_e2_flujo_comprehension():
    codigo = get_file_contents('./python_course/c4/e2_flujo_comprehension.txt')
    resultado = list()
    results = [(codigo, resultado)]
    return render_template("c2_servidor.html", template_vars={'results': results})

@app.route('/flujo/others')
def c4_e2_flujo_others():
    codigo = get_file_contents('./python_course/c4/e2_flujo_others.txt')
    resultado = list()
    results = [(codigo, resultado)]
    return render_template("c2_servidor.html", template_vars={'results': results})

@app.route('/<chapter>/<example>')
def show_code(chapter, example):
    try:
        module = import_module('%s.%s' % (chapter, example))
        codigo = get_source_lines(module)
        resultado = list()
        results = [(codigo, resultado)]

    except Exception as e:
        codigo = repr(e)
        results = list()

    return render_template("c2_servidor.html", template_vars={'results': results})

if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = 'AhLae9chahKua5fuZia7ooji'
    toolbar = DebugToolbarExtension(app)
    app.run(host="0.0.0.0", port=5000)
