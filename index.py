from distutils.log import debug
from flask import Flask, render_template 

app = Flask(__name__)

# Rutas principales

@app.route('/') #Ruta para pagina principal
def home():
    return render_template('home.html')

@app.route('/edificios/edificio_a')
def edificio_a():
    return render_template('/edificios/edificio_a.html')

@app.route('/edificios_externos')
def edificios_externos():
    return render_template('/edificios/edificios_externos.html')

@app.route('/edificio_gerencial')
def edificio_gerencial():
    return render_template('/edificios/edificio_gerencial.html')

@app.route('/edificio_central')
def edificio_central():
    return render_template('/edificios/edificio_central.html')

@app.route('/sub_suelo')
def sub_suelo():
    return render_template('/edificios/sub_suelo.html')

@app.route('/equipo/computadora_informacion.html')
def computadora_informacion():
    return render_template('/equipo/computadora_informacion.html')

# Rutas de pisos del Edificio Central

@app.route('/edificio_central/ec_subsuelo')
def ec_subsuelo():
    return render_template('/edificios/edificio_central/ec_subsuelo.html')

@app.route('/edificio_central/ec_planta_baja')
def ec_planta_baja():
    return render_template('/edificios/edificio_central/ec_planta_baja.html')

@app.route('/edificio_central/ec_primer_piso')
def ec_primer_piso():
    return render_template('/edificios/edificio_central/ec_primer_piso.html')

@app.route('/edificio_central/ec_segundo_piso')
def ec_segundo_piso():
    return render_template('/edificios/edificio_central/ec_segundo_piso.html')

@app.route('/edificio_central/ec_tercer_piso')
def ec_tercer_piso():
    return render_template('/edificios/edificio_central/ec_tercer_piso.html')

@app.route('/edificio_central/ec_cuarto_piso')
def ec_cuarto_piso():
    return render_template('/edificios/edificio_central/ec_cuarto_piso.html')

@app.route('/edificio_central/ec_quinto_piso')
def ec_quinto_piso():
    return render_template('/edificios/edificio_central/ec_quinto_piso.html')

# Rutas de departamentos del subsuelo

@app.route('/sub_suelo/sistemas')
def sistemas():
    return render_template('/edificios/subsuelo/sistemas.html')

@app.route('/sub_suelo/honorarios')
def honorarios():
    return render_template('/edificios/subsuelo/honorarios.html')

@app.route('/sub_suelo/doc_investigacion')
def doc_investigacion():
    return render_template('/edificios/subsuelo/doc_investigacion.html')

@app.route('/sub_suelo/atp')
def atp():
    return render_template('/edificios/subsuelo/atp.html')

@app.route('/sub_suelo/marketing')
def marketing():
    return render_template('/edificios/subsuelo/marketing.html')

@app.route('/sub_suelo/salon_actos')
def salon_actos():
    return render_template('/edificios/subsuelo/salon_actos.html')

@app.route('/sub_suelo/rel_publicas')
def rel_publicas():
    return render_template('/edificios/subsuelo/rel_publicas.html')







if __name__ == '__main__': 
    app.run(debug=True)

