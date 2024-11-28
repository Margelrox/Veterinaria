from model.Perro import Perro
from model.conexionBDD import conectar_bd


def listaPerros():
    conn=conectar_bd()
    cursor=conn.cursor()
    query="SELECT * FROM perros"
    cursor.execute(query)
    perros=cursor.fetchall()
    for perro in perros:
        print(f"ID: {perro[0]}, Nombre: {perro[1]}, Color: {perro[2]}, Edad: {perro[3]}")
    cursor.close()
    conn.close()

def agregarPerro(perro):
    conn = conectar_bd()
    cursor = conn.cursor()
    query = "INSERT INTO perros (nombre, color, edad) VALUES (%s, %s, %s)"
    values = (perro.getNombre(), perro.getColor(), perro.getEdad())
    cursor.execute(query, values)
    conn.commit()
    print(f"Perro {perro.getNombre()}, Insertado correctamente")
    cursor.close()
    conn.close()
    
    

def editarPerro(id_perro, nuevo_nombre=None, nuevo_color=None, nueva_edad=None):

    conn=conectar_bd()
    cursor=conn.cursor()
    query="UPDATE perros SET "
    updates = []
    values = []
    if nuevo_nombre:
        updates.append("nombre = %s")
        values.append(nuevo_nombre)
    
    if nuevo_color:
        updates.append("color = %s")
        values.append(nuevo_color)
    
    if nueva_edad:
        updates.append("edad = %s")
        values.append(nueva_edad)

    query += ", ".join(updates)+ " WHERE id_perro = %s"
    values.append(id_perro)
    cursor.execute(query, tuple(values))
    conn.commit()

    cursor.close()
    conn.close()



def eliminarPerro(id_perro):
    conn= conectar_bd()
    cursor = conn.cursor()
    query="DELETE FROM perros WHERE id_perro = %s"
    cursor.execute(query, (id_perro,))
    conn.commit()
    print(f"Perro con ID: {id_perro} Eliminado correctamente")
    cursor.close()
    conn.close()