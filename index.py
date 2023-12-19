from distutils.log import debug
from flask import Flask, render_template 

app = Flask(__name__)

# Rutas principales

@app.route('/') #Ruta para pagina principal
def home():
    return render_template('home.html')

@app.route('/edificio_a')
def edificio_a():
    return render_template('edificio_a.html')

@app.route('/edificios_externos')
def edificios_externos():
    return render_template('edificios_externos.html')

@app.route('/edificio_gerencial')
def edificio_gerencial():
    return render_template('edificio_gerencial.html')

@app.route('/edificio_central')
def edificio_central():
    return render_template('/edificios/edificio_central.html')

@app.route('/sub_suelo')
def sub_suelo():
    return render_template('sub_suelo.html')


# Rutas secundarias 

@app.route('/edificio_central/ec_subsuelo')
def ec_subsuelo():
    return render_template('/edificios/edificio_central/ec_subsuelo.html')



if __name__ == '__main__': 
    app.run(debug=True)

