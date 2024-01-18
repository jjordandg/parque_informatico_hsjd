from distutils.log import debug
from flask import Flask, render_template 
from controlador import obtenerEquipo, obtenerSectores, obtenerEquiposSector
app = Flask(__name__)

# Rutas principales

@app.route('/') #Ruta para pagina principal
def home():
    return render_template('home.html')


#Ruta con parametros
@app.route('/<edificio>')
def sectores_por_edificio(edificio):
    sectores = obtenerSectores(edificio)
    return render_template('/sectores.html', sectores=sectores)


@app.route('/<edificio>/<sector>')
def equipos_por_sector(edificio, sector):
    equipos = obtenerEquiposSector(edificio, sector)
    return render_template('/equipos.html', equipos=equipos)

# @app.route('<edificio>/<piso>/<sector>/<id_equipo>')
# def equipos_por_sector(edificio, piso, sector, id_equipo):
#     equipos = obtenerEquipos(edificio, piso, sector, id_equipo)
#     return render_template('/computadora_informacion.html', equipos=equipos)

#Ruta que trae el equipo por ID evaluando el edificio y sector 
@app.route('/computadora_informacion.html')
def computadora_informacion(edificio, sector, id):
    equipo = obtenerEquipo(edificio, sector, id)
    return render_template('/computadora_informacion.html', equipo=equipo)

if __name__ == '__main__': 
    app.run(debug=True)

