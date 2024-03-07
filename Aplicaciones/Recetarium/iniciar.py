import mysql.connector

# Datos de conexión a la base de datos
hostname = 'localhost'  # Nombre del servidor
username = 'root'   # Nombre de usuario de la base de datos
password = ''   # Contraseña de la base de datos
database = 'recetariumv7alpha'   # Nombre de la base de datos

try:
    # Crear conexión
    conn = mysql.connector.connect(
        host=hostname,
        user=username,
        password=password,
        database=database
    )

    # Verificar si la conexión está establecida correctamente
    if conn.is_connected():
        print("Conexión exitosa")

except mysql.connector.Error as e:
    print(f"Error al conectar a la base de datos: {e}")

finally:
    # Cerrar conexión
    if 'conn' in locals() and conn.is_connected():
        conn.close()
