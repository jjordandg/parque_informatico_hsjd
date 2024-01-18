import pymysql

def crearConexion():
    try:
        conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='Contratiemp0$',
            db='db_hsjd'
        )
        return conexion

    except pymysql.Error as e:
        # Manejar errores de conexión
        print(f"Error de conexión a la base de datos: {e}")
        raise
