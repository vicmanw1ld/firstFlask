from crypt import methods
from flask import Flask, render_template, request, session, url_for
from werkzeug.utils import redirect
from werkzeug.exceptions import abort
from flask import jsonify    
from flask import send_file

app = Flask(__name__)

app.secret_key = 'mi_llave_secreta'

@app.route("/", methods=['GET', 'POST'])
def inicio():
    if 'username' in session:
        return render_template('index.html')
    return render_template('login.html')    
    
      
@app.route('/login', methods=['GET', 'POST'])
def login():
    # no se va a validar el user
    if request.method == 'POST':
        session['username'] = request.form['username']
        # agregamos el usuario a la seession, sería como poner
        # usuario = request.form['username'] (form es nuestro formulario)
        # session['username'] = usuario
        return redirect(url_for('inicio'))
    return render_template('login.html')

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('error404.html', error=error), 404


@app.route('/salir')
def salir():
    return abort(404)
    
@app.route('/logout')
def logout():
    session.pop('username')
    return redirect(url_for('login'))    


# @app.route('/principio', methods=['GET', 'POST'])
# def principio():
#     return render_template('FlaskPython.html')


# @app.route('/redireccionar')
# def redireccionar():
#     return redirect(url_for('inicio'))





# rest represantiotional state transfer
# api 
# @app.route('/api/mostrar/<nombre>',methods=['GET' 'POST'])
# def mostrar_json(nombre):
#     valores = {'nombre': nombre, 'metodo_http': request.method}
#     return jsonify(valores)




    
