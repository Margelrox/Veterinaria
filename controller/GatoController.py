from model.Gato import Gato
from model.conexionBDD import conectar_bd


def listaGatos():
    conn=conectar_bd()
    cursor=conn.cursor()
    query="SELECT * FROM gatitos"
    cursor.execute(query)
    gatos=cursor.fetchall()
    for gato in gatos:
        print(f"ID: {gato[0]}, Nombre: {gato[1]}, Color: {gato[2]}, Edad: {gato[3]}")
    cursor.close()
    conn.close()

def agregarGatos(gato):
    conn = conectar_bd()
    cursor = conn.cursor()
    query = "INSERT INTO gatitos (nombre, color, edad) VALUES (%s, %s, %s)"
    values = (gato.getNombre(), gato.getColor(), gato.getEdad())
    cursor.execute(query, values)
    conn.commit()
    print(f"Gato {gato.getNombre()}, Insertado correctamente")
    cursor.close()
    conn.close()
    
    

def editarGato(id_gatito, nuevo_nombre=None, nuevo_color=None, nueva_edad=None):

    conn=conectar_bd()
    cursor=conn.cursor()
    query="UPDATE gatitos SET "
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

    query += ", ".join(updates)+ " WHERE id_gatito = %s"
    values.append(id_gatito)
    cursor.execute(query, tuple(values))
    conn.commit()

    cursor.close()
    conn.close()



def eliminarGato(id_gatito):
    conn= conectar_bd()
    cursor = conn.cursor()
    query="DELETE FROM gatitos WHERE id_gatito = %s"
    cursor.execute(query, (id_gatito,))
    conn.commit()
    print(f"Gatito con ID: {id_gatito} Eliminado correctamente")
    cursor.close()
    conn.close()