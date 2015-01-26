__author__ = 'jesus.pedro.gutierrez.almazan'
import c2.servidor
from flask import Flask
from tools.utils import get_source_lines
from flask.templating import render_template
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Controlador para el directorio principal.
    Por cada codigo, se genera una tupla codigo, resultados
    codigo lista de cadenas que son las lineas de un codigo
    resultado es una lista con los resultados de la ejecucion del anterior codigo
    """
    # codigo es una lista de cadenas que representan lineas de codigo
    codigo = get_source_lines(c2.servidor)
    
    # resultado es una lista con los resultados obtenidos en la ejecucion del codigo anterior
    resultado = list()
    
    # results es una lista de pares codigo, resultado
    # la plantilla recogera pares de codigo,resultados y los pintara
    results = [(codigo, resultado)]
    return render_template("c2_servidor.html", template_vars={'results': results})

if __name__ == '__main__':
    app.debug = True
    app.config['SECRET_KEY'] = 'AhLae9chahKua5fuZia7ooji'
    toolbar = DebugToolbarExtension(app)
    app.run(host="0.0.0.0", port=5000)