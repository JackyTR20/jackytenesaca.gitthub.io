import mysql.connector

def connectionBD():
    # Configuración de las credenciales
    credenciales = {
        "host": "35.227.152.71",
        "user": "root",
        "password": "sky2003-04",
        "database": "proyecto_integrador",
        "charset": "utf8mb4",
        "collation": "utf8mb4_unicode_ci",
    }

    try:
        # Conexión a la base de datos
        conexion = mysql.connector.connect(**credenciales)

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion

    except mysql.connector.Error as error:
        print(f"No se pudo conectar a la base de datos: {error}")

# Ejemplo de uso
conexion_bd = connectionBD()
# Ahora puedes realizar operaciones en la base de datos usando la conexión
