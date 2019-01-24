import sqlite3
import os
import sys

try:

    bbdd = 'provinciaslocalidades'
    conex = sqlite3.connect(bbdd)
    cur = conex.cursor()
    print('Base de datos de provincias conectada')

except:
    print ("Posibles errores de importacion")
    sys.exit(1)


#cargar combo provincias al iniciar el programa
def cargarcmbprov(listprovincias):
    try:
        cur.execute("select provincia from provincias")
        rows = cur.fetchall()

        for row in rows:
            listprovincias.append(row)
    except:
        conex.rollback

def llenarLocalidades(provincia, listlocalidades, cmblocalidad):
    try:

        cur.execute("select municipio from municipios where provincia_id=(select id from Provincias where id="+str((provincia)+1)+")")

        listado = cur.fetchall()
        cmblocalidad.set_button_sensitivity(True)

        for row in listado:
            listlocalidades.append(row)


    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback

def recuperarprovincia(provincia):
    try:
        cur.execute("select id from provincias where provincia ='" + provincia + "'")

        idprovincia = cur.fetchall()

        return idprovincia[0][0]-1


    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback

def recuperarlocalidad(localidad,provincia):
    try:
        cur.execute("select id from municipios where municipio='"+localidad+"'")
        idlocalidad = cur.fetchall()
        cur.execute("select min(id),max(id) from municipios where provincia_id ='" + str(provincia) + "'")
        minmax = cur.fetchall()
        numero = minmax[0][1]-minmax[0][0]
        pos=numero-(minmax[0][1]-idlocalidad[0][0])

        return pos


    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback