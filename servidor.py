# -*- coding: utf-8 -*-
__author__ = 'jesus.pedro.gutierrez.almazan'

<<<<<<< HEAD
from c2 import servidor

=======
>>>>>>> f8a536bd2975540a3e60d070f31629d1b423921a
from tools.utils import get_source_lines, get_file_contents

from flask import Flask
from flask.templating import render_template
from flask_debugtoolbar import DebugToolbarExtension

import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    codigo = get_source_lines(servidor)
    resultado = list()
    results = [(codigo, resultado)]
    return render_template("c2_servidor.html", template_vars={'results': results})

@app.route('/<chapter>/<example>')
def show_code(chapter, example):
    path = os.path.join(os.path.dirname(__name__), "templates", "code_examples", chapter, "%s.txt" % example)
    codigo = get_file_contents(path)
    resultado = list()
    results = [(codigo, resultado)]
    return render_template("c2_servidor.html", template_vars={'results': results})



if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = 'AhLae9chahKua5fuZia7ooji'
    toolbar = DebugToolbarExtension(app)
    app.run(host="0.0.0.0", port=5000)

