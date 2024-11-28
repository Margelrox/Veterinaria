import mysql.connector
import bcrypt

def conectar_bd():
    return mysql.connector.connect(
        host='localhost',
        user='usuariopoos',
        password='usuariopoos',
        database='veterinaria',
    )
        
def autenticar_usuario(correo,contrasena):
    conn=conectar_bd()
    cursor=conn.cursor()

    #query = "SELECT * FROM usuarios WHERE correo = %s AND contrasena = %s"
    query = "SELECT contrasena FROM usuarios WHERE correo = %s"
    cursor.execute(query, (correo, ))

    resultado = cursor.fetchone()

    conn.close()
    
    if not resultado:
        return False
    hash_password = resultado[0]
    return bcrypt.checkpw(contrasena.enconde('utf-8'), hash_password.enconde('utf-8'))

def registrar_usuario(correo,contrasena):
    salt = bcrypt.gensalt()
    hash_password = bcrypt.hashpw(contrasena.encode('utf-8'), salt)
    conn=conectar_bd()
    cursor=conn.cursor()

    query = "INSERT INTO usuarios (correo, contrasena) VALUES (%s,%s)"
    values = (correo,hash_password)

    cursor.execute(query,values)
    conn.commit()
    cursor.close()
    conn.close()