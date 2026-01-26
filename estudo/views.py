from estudo import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    usuario = 'Raphael'
    idade = 23

    context = {
        'usuario': usuario,
        'idade':idade
    }
    return render_template('index.html', context = context )

@app.route('/contato/')
def novapag():
    return 'outra view '