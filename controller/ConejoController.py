from model.Conejo import Conejo
from model.conexionBDD import conectar_bd


def listaConejos():
    conn=conectar_bd()
    cursor=conn.cursor()
    query="SELECT * FROM conejos"
    cursor.execute(query)
    conejos=cursor.fetchall()
    for conejo in conejos:
        print(f"ID: {conejo[0]}, Nombre: {conejo[1]}, Color: {conejo[2]}, Edad: {conejo[3]}")
    cursor.close()
    conn.close()

def agregarConejos(conejo):
    conn = conectar_bd()
    cursor = conn.cursor()
    query = "INSERT INTO conejos (nombre, color, edad) VALUES (%s, %s, %s)"
    values = (conejo.getNombre(), conejo.getColor(), conejo.getEdad())
    cursor.execute(query, values)
    conn.commit()
    print(f"Conejo {conejo.getNombre()}, Insertado correctamente")
    cursor.close()
    conn.close()
    
    

def editarConejos(id_conejo, nuevo_nombre=None, nuevo_color=None, nueva_edad=None):

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

    query += ", ".join(updates)+ " WHERE id_conejo = %s"
    values.append(id_conejo)
    cursor.execute(query, tuple(values))
    conn.commit()

    cursor.close()
    conn.close()



def eliminarConejo(id_conejo):
    conn= conectar_bd()
    cursor = conn.cursor()
    query="DELETE FROM gatitos WHERE id_conejo = %s"
    cursor.execute(query, (id_conejo,))
    conn.commit()
    print(f"Gatito con ID: {id_conejo} Eliminado correctamente")
    cursor.close()
    conn.close()