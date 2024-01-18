from bd import crearConexion


def obtenerEquipo(id_equipo):
    conexion = crearConexion()
    equipo = []
    with conexion.cursor() as cursor:
        query = "SELECT * FROM bd_hsjd.equipos_hsjd WHERE ID = %s"
        cursor.execute(query, (id_equipo))
        equipo = cursor.fetchone()
    conexion.close()
    return equipo

def obtenerSectores(edificio):
    conexion = crearConexion()
    sectores = []
    with conexion.cursor() as cursor:
        query = "SELECT SECTOR, SECTORKEY FROM db_hsjd.equipos_hsjd WHERE BUILDINGKEY = %s"
        cursor.execute(query, (edificio))
        sectores = cursor.fetchall()
    conexion.close()
    return sectores

def obtenerEquiposSector(edificio, sector):
    conexion = crearConexion()
    equipos = []
    with conexion.cursor() as cursor:
        query = "SELECT ID, IP, HOSTNAME FROM db_hsjd.equipos_hsjd WHERE BUILDINGKEY = %s && SECTORKEY = %s"
        cursor.execute(query, (edificio, sector))
        equipos = cursor.fetchall()
    conexion.close()
    return equipos

# def obtenerEquipos(edificio, sector):
#     conexion = crearConexion()
#     equipos = []
#     with conexion.cursor() as cursor:
#         query = "SELECT ID, IP, HOSTNAME FROM db_hsjd.equipos_hsjd WHERE BUILDING-KEY = %s && FLOOR-KEY = %s"
#         cursor.execute(query, (edificio), (sector))
#         equipos = cursor.fetchall()
#     conexion.close()
#     return equipos



# Ejemplo para acceder a datos de una tupla indexada usando un for para recorrerla 

# for persona in personas:
#     nombre = persona[column_mapping['nombre']]
#     print(f"Nombre: {nombre}")

# column_mapping['nombre'] te dará el índice correspondiente a la columna 'nombre', y puedes usar ese índice para acceder al nombre de cada persona en el bucle.