from fileinput import filename
from flask import Flask, render_template, url_for

app = Flask("__name__")

@app.route('/')
def tela_inicial():
    url_for('static',filename='styles/estilo.css')
    return render_template('index.html')

@app.route('/quem-somos')
def quem_somos():
    url_for('static',filename='styles/estilo.css')
    return render_template('quem-somos.html')

@app.route('/contato')
def contato():
    url_for('static',filename='styles/estilo.css')
    return render_template('contato.html')

