import os
import sqlite3



try:
    bbdd = 'restaurante'
    conex = sqlite3.connect(bbdd)
    cur= conex.cursor()
    print('Base de datos conectada')

except sqlite3.OperationalError as e:
    print(e)

def cerrarconexion():

    try:
        conex.commit()
        conex.close()
        print('Base de datos cerrada')

    except sqlite3.OperationalError as e:
        print(e)

#Método para cargar mesas al arrancar el programa
def cargarMesas(listmesas,treemesas):
    try:
        listmesas.clear()
        cur.execute("select * from Mesa")
        cursor=cur.fetchall()
        for row in cursor:
            cargarMesasTree(treemesas,listmesas,row)

    except sqlite3.OperationalError as e:
        print(e)


def cargarMesas2(listmesas2,treemesas2):
    confirmacion = 'Si'
    try:
        listmesas2.clear()
        cur.execute("select Idmesa, Maxcomensales from Mesa where Ocupada = '"+ confirmacion +"' ")
        cursor=cur.fetchall()
        for row in cursor:
            listmesas2.append(row)
            treemesas2.show()

    except sqlite3.OperationalError as e:
        print(e)


#Método para cargar las mesas en el treeview
def cargarMesasTree(treemesas,listmesas,fila):
    listmesas.append(fila)
    treemesas.show()


#Método para comprobar el login del camarero
def comprobarlogin(nombre,contraseña):
    try:

        cur.execute("select Idcamarero from Camarero where Nombre=? and Contraseña=?",(nombre,contraseña))
        cursor=cur.fetchall()
        return cursor


    except sqlite3.OperationalError as e:
        print(e)

def comprobarcamarero(nombre):
    try:

        cur.execute("select Idcamarero from Camarero where Nombre=?",(nombre,))
        cursor=cur.fetchall()

        return cursor


    except sqlite3.OperationalError as e:
        print(e)

#Método para cambiar el estado de una mesa al pulsar ocupar mesa
def cambiarestadomesa(idmesa):
    confirmación = 'Si'
    try:
        cur.execute("Update Mesa set Ocupada=? where Idmesa =?",(confirmación,idmesa))
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()

#Método para cambiar el estado de una mesa al pulsar vaciar mesa
def cambiarestadomesavaciar(idmesa):
    confirmación = 'No'
    try:
        cur.execute("Update Mesa set Ocupada=? where Idmesa =?",(confirmación,idmesa))
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()


def cargaImagenesMesas(ListaMesas, mesa1, mesa2, mesa3, mesa4, mesa5, mesa6, mesa7, mesa8, image1, image2, image3, image4, image5, image6, image7, image8):
    try:
        ListaMesas.clear()

        cur.execute("SELECT * FROM Mesa")
        cursor = cur.fetchall()
        for row in cursor:
            if row[2] == 'Si':
                if row[0] == 1:
                    image1.set_from_file("../imagenes/mesa4ocupada.png");
                    mesa1.set_sensitive(False)
                if row[0] == 2:
                    image2.set_from_file("../imagenes/mesa4ocupada.png");
                    mesa2.set_sensitive(False)
                if row[0] == 3:
                    image3.set_from_file("../imagenes/mesa4ocupada.png");
                    mesa3.set_sensitive(False)
                if row[0] == 4:
                    image4.set_from_file("../imagenes/mesa4ocupada.png");
                    mesa4.set_sensitive(False)
                if row[0] == 5:
                    image5.set_from_file("../imagenes/mesa8ocupada.png");
                    mesa5.set_sensitive(False)
                if row[0] == 6:
                    image6.set_from_file("../imagenes/mesa8ocupada.png");
                    mesa6.set_sensitive(False)
                if row[0] == 7:
                    image7.set_from_file("../imagenes/mesa10ocupada.png");
                    mesa7.set_sensitive(False)
                if row[0] == 8:
                    image8.set_from_file("../imagenes/mesa10ocupada.png");
                    mesa8.set_sensitive(False)

    except sqlite3.OperationalError as e:
        print(e)


def altacliente(fila):
    try:
        cur.execute("Insert into Cliente (DNI,Apellidos,Nombre,Dirección,Provincia,Ciudad) values (?,?,?,?,?,?)",fila)
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()

def cargarClientes(listclientes,treeclientes):
    try:
        listclientes.clear()
        cur.execute("select * from Cliente")
        cursor=cur.fetchall()
        for row in cursor:
            listclientes.append(row)
            treeclientes.show()

    except sqlite3.OperationalError as e:
        print(e)


def modificarCliente(fila):
    try:
        cur.execute("Update Cliente set DNI=?,Apellidos=?,Nombre=?,Dirección=?,Provincia=?,Ciudad=?"
                    " where DNI=? ",(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[0]))
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()


def altacamarero(nombre,contraseña):
    try:
        cur.execute("Insert into Camarero (Nombre,Contraseña) values ('"+nombre+"','"+contraseña+"')")
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()


def altaproducto(nombre,precio):
    try:
        cur.execute("Insert into Producto (Nombreproducto, Preciounidad) values ('"+nombre+"','"+precio+"')")
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()


def cargarproductos(listproductos,treeproductos):
    try:
        listproductos.clear()
        cur.execute("select * from Producto")
        cursor=cur.fetchall()

        i = 0
        for row in cursor:
            id = int(row[0])
            nombre = row[1]
            precio = str(row[2])
            fila = (id, nombre, precio)
            listproductos.append(fila)
            treeproductos.show()
            i = i + 1

    except sqlite3.OperationalError as e:
        print(e)

def crearfactura(fila):
    try:
        cur.execute("Insert into Factura (Idcamarero,Idmesa,Fecha) values (?,?,?)",fila)
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()

def cargarfacturasmesa(treefacturas,listfacturas,idmesa):
    try:
        listfacturas.clear()
        cur.execute("select Idfactura, Idcamarero, Idmesa, Fecha, Pagada from Factura where Idmesa = '" + str(idmesa) + "'")
        cursor=cur.fetchall()
        for row in cursor:
            listfacturas.append(row)
            treefacturas.show()

    except sqlite3.OperationalError as e:
        print(e)

def buscarproducto(producto):
    try:
        cur.execute("select Idproducto from Producto where Nombreproducto = '" + producto + "'")
        cursor=cur.fetchall()
        print (cursor)
        return cursor [0][0]

    except sqlite3.OperationalError as e:
        print(e)

def altalineaproducto(idfactura,idproducto,cantidad):
    try:
        cur.execute("Insert into Lineafactura (Idfactura,Idproducto,Cantidad) values ('"+str(idfactura)+"','"+str(idproducto)+"','"+str(cantidad)+"')")
        conex.commit()
    except sqlite3.OperationalError as e:
        print(e)
        conex.rollback()

def comprobarcamarerofactura(camarero,idfactura):
    try:
        cur.execute("select Idcamarero from Camarero where Nombre=?", (camarero,))
        cursor = cur.fetchall()

        cur.execute("select Idcamarero from Factura where Idfactura=?", (idfactura,))
        cursor2 = cur.fetchall()


        if cursor == cursor2:
            return True
        else:
            return False

    except sqlite3.OperationalError as e:
        print(e)


def cargarfacturas(listfacturas2,treefacturas2):
    try:
        listfacturas2.clear()
        cur.execute("select * from Factura")
        cursor=cur.fetchall()
        for row in cursor:
            listfacturas2.append(row)
            treefacturas2.show()

    except sqlite3.OperationalError as e:
        print(e)

def pagarfactura(idfactura,pagada):
    try:
        cur.execute("Update Factura set Pagada=? where Idfactura=? ", (pagada, idfactura,))
        conex.commit()

    except sqlite3.OperationalError as e:
        print(e)

def buscarmesafactura(idfactura):
    try:
        cur.execute("select Idmesa from Factura where Idfactura = '" + idfactura + "'")
        cursor=cur.fetchall()
        return cursor [0][0]

    except sqlite3.OperationalError as e:
        print(e)

