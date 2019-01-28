import gi
import datos
import datosprovincias

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Restaurante:
    def __init__(self):
        # iniciamos la libreria GTK
        b = Gtk.Builder()
        b.add_from_file('venrestaurante.glade')

        #Objetos ventana principal
        self.venprincipal = b.get_object("venprincipal")
        self.btnmesa1 = b.get_object("btnmesa1")
        self.btnmesa2 = b.get_object("btnmesa2")
        self.btnmesa3 = b.get_object("btnmesa3")
        self.btnmesa4 = b.get_object("btnmesa4")
        self.btnmesa5 = b.get_object("btnmesa5")
        self.btnmesa6 = b.get_object("btnmesa6")
        self.btnmesa7 = b.get_object("btnmesa7")
        self.btnmesa8 = b.get_object("btnmesa8")
        self.nbook = b.get_object("nbook")
        self.toollimpiar = b.get_object("toollimpiar")
        self.toolsalir = b.get_object("toolsalir")
        self.menuabrirsesion = b.get_object("menuabrirsesion")
        self.menucerrarsesion = b.get_object("menucerrarsesion")
        self.menuregistrarsesion = b.get_object("menuregistrarsesion")
        self.mesa1 = b.get_object("mesa1")
        self.mesa2 = b.get_object("mesa2")
        self.mesa3 = b.get_object("mesa3")
        self.mesa4 = b.get_object("mesa4")
        self.mesa5 = b.get_object("mesa5")
        self.mesa6 = b.get_object("mesa6")
        self.mesa7 = b.get_object("mesa7")
        self.mesa8 = b.get_object("mesa8")
        self.lbllogin = b.get_object("lbllogin")


        #Objetos pestaña mesas
        self.lblmesa = b.get_object("lblmesa")
        self.lblcamarero = b.get_object("lblcamarero")
        self.btnocuparmesa = b.get_object("btnocuparmesa")
        self.btnlogincamarero = b.get_object("btnlogincamarero")
        self.treemesas = b.get_object("treemesas")
        self.listmesas = b.get_object("listmesas")
        self.btnvaciarmesa = b.get_object("btnvaciarmesa")

        # Objetos pestaña clientes
        self.entdni = b.get_object("entdni")
        self.entapellidos = b.get_object("entapellidos")
        self.entnombre = b.get_object("entnombre")
        self.entdireccion = b.get_object("entdireccion")
        self.cmbprovincia = b.get_object("cmbprovincia")
        self.cmblocalidad = b.get_object("cmblocalidad")
        self.listprovincias = b.get_object("listprovincias")
        self.listlocalidades = b.get_object("listlocalidades")
        self.btnaltacliente = b.get_object("btnaltacliente")
        self.btnmodcliente = b.get_object("btnmodcliente")
        self.listclientes = b.get_object("listclientes")
        self.treeclientes = b.get_object("treeclientes")

        #Objetos pestaña productos
        self.lblmesaservicio = b.get_object("lblmesaservicio")
        self.lblproducto = b.get_object("lblproducto")
        self.entproducto = b.get_object("entproducto")
        self.btnañadirproducto = b.get_object("btnañadirproducto")


        #Objetos ventana añadir productos
        self.venproductos = b.get_object("venproductos")
        self.entnombreproducto = b.get_object("entnombreproducto")
        self.entprecio = b.get_object("entprecio")
        self.btnprodvolver = b.get_object("btnprodvolver")
        self.btnañadirprod = b.get_object("btnañadirprod")


        #Objetos ventana login camareros
        self.venlogin = b.get_object("venlogin")
        self.entnombrecamarero = b.get_object ("entnombrecamarero")
        self.entcontraseña = b.get_object("entcontraseña")
        self.btnvolver = b.get_object("btnvolver")
        self.btnconfirmarlogin = b.get_object("btnconfirmarlogin")

        #Objetos ventana registrar nuevo camarero
        self.venregistrar = b.get_object("venregistrar")
        self.entregnombrecamarero = b.get_object("entregnombrecamarero")
        self.entregcontraseña = b.get_object("entregcontraseña")
        self.entregconfirmarcontraseña = b.get_object("entregconfirmarcontraseña")
        self.btnregvolver = b.get_object("btnregvolver")
        self.btnregistrar = b.get_object("btnregistrar")


        #Objetos ventana aviso login
        self.venerror = b.get_object("venerror")
        self.btnaceptarerrorlogin = b.get_object("btnaceptarerrorlogin")

        # Objetos ventana aviso registrar
        self.venavisoroot = b.get_object("venvisoroot")
        self.btnaceptar = b.get_object("btnaceptar")

        #Objetos ventana aviso ocuparmesa
        self.venerror2 = b.get_object("venerror2")
        self.btnaceptar2 = b.get_object("btnaceptar2")



        #Diccionario de eventos

        dic = {'on_venprincipal_destroy': self.salir,
               'on_btnmesa1_clicked': self.pulsarbtnmesa1,
               'on_btnmesa2_clicked': self.pulsarbtnmesa2,
               'on_btnmesa3_clicked': self.pulsarbtnmesa3,
               'on_btnmesa4_clicked': self.pulsarbtnmesa4,
               'on_btnmesa5_clicked': self.pulsarbtnmesa5,
               'on_btnmesa6_clicked': self.pulsarbtnmesa6,
               'on_btnmesa7_clicked': self.pulsarbtnmesa7,
               'on_btnmesa8_clicked': self.pulsarbtnmesa8,
               'on_btnlogincamarero_clicked': self.showvenlogin,
               'on_btnocuparmesa_clicked': self.cambiarestadomesa,
               'on_btnvolver_clicked': self.hidevenlogin,
               'on_btnconfirmarlogin_clicked': self.confirmarlogin,
               'on_btnaceptarerrorlogin_clicked': self.hidevenerror,
               'on_btnaceptar2_clicked': self.hidevenerror2,
               'on_treemesas_cursor_changed': self.recuperarmesa,
               'on_btnvaciarmesa_clicked': self.vaciarmesa,
               'on_toolsalir_clicked': self.salir,
               'on_cmbprovincia_changed': self.cargarlocalidadescmb,
               'on_btnaltacliente_clicked': self.altaCliente,
               'on_toollimpiar_clicked': self.limpiarcampos,
               'on_treeclientes_cursor_changed': self.recuperarcliente,
               'on_btnmodcliente_clicked': self.modificarcliente,
               'on_menuabrirsesion_activate': self.abrirsesion,
               'on_menucerrarsesion_activate': self.cerrarsesion,
               'on_menuregistrarcamarero_activate': self.registrarcamarero,
               'on_btnaceptar_clicked': self.hidevenavisoroot,
               'on_btnregvolver_clicked':self.hidevenregistrar,
               'on_btnregistrar_clicked': self.btnregistrarcamarero }

        b.connect_signals(dic)
        self.venprincipal.show()
        self.venprincipal.fullscreen()
        self.venlogin.connect('delete-event', lambda w, e: w.hide() or True)
        self.venerror.connect('delete-event', lambda w, e: w.hide() or True)
        self.venerror2.connect('delete-event', lambda w, e: w.hide() or True)
        self.venregistrar.connect('delete-event', lambda w, e: w.hide() or True)
        #self.venavisoroot.connect('delete-event', lambda w, e: w.hide() or True)
        datosprovincias.cargarcmbprov(self.listprovincias)
        datos.cargaImagenesMesas(self.listmesas, self.btnmesa1, self.btnmesa2, self.btnmesa3,
                                  self.btnmesa4,self.btnmesa5,self.btnmesa6,self.btnmesa7,self.btnmesa8,self.mesa1,
                                  self.mesa2,self.mesa3,self.mesa4,self.mesa5,self.mesa6,self.mesa7,self.mesa8)
        datos.cargarMesas(self.listmesas, self.treemesas)
        datos.cargarClientes(self.listclientes, self.treeclientes)



    def salir(self, widget, data=None):
        Gtk.main_quit()

    def showvenlogin(self, widget, data=None):
        self.venlogin.show()

    def hidevenlogin(self, widget, data=None):
        self.venlogin.hide()

    def hidevenerror(self, widget, data=None):
        self.venerror.hide()

    def hidevenerror2(self, widget, data=None):
        self.venerror2.hide()

    def hidevenavisoroot(self, widget, data=None):
        self.venavisoroot.hide()

    def hidevenregistrar(self, widget, data=None):
        self.venregistrar.hide()

    def confirmarlogin(self, widget, data=None):
        nombre = self.entnombrecamarero.get_text()
        contraseña = self.entcontraseña.get_text()
        idcamarero = datos.comprobarlogin(nombre,contraseña)
        if idcamarero != []:
            self.lblcamarero.set_text(nombre)
            self.lbllogin.set_text("Usuario: " + nombre)
            self.entnombrecamarero.set_text('')
            self.entcontraseña.set_text('')
            self.venlogin.hide()
        else :
            self.venerror.show()

    def abrirsesion(self,widget, data=None):
        self.venlogin.show()

    def cerrarsesion(self,widget, data=None):
        self.lblcamarero.set_text('')
        self.lbllogin.set_text('')

    def registrarcamarero(self, widget, data=None):
        usuario = self.lblcamarero.get_text()
        if usuario == 'root':
            self.venregistrar.show()
        else :
            self.venerror.show()

    def btnregistrarcamarero(self,widget,data=None):
        nombre = self.entregnombrecamarero.get_text()
        contraseña = self.entregcontraseña.get_text()
        confcontraseña = self.entregconfirmarcontraseña.get_text()
        print(nombre,contraseña)

        if contraseña == confcontraseña:
            datos.altacamarero(nombre,contraseña)
            self.venregistrar.hide()



    def pulsarbtnmesa1(self,widget, data=None):
        self.lblmesa.set_text("Mesa 1 (4 comensales)")
        self.btnocuparmesa.set_sensitive(True)
        self.btnvaciarmesa.set_sensitive(False)

    def pulsarbtnmesa2(self,widget, data=None):
        self.lblmesa.set_text("Mesa 2 (4 comensales)")
        self.btnocuparmesa.set_sensitive(True)
        self.btnvaciarmesa.set_sensitive(False)

    def pulsarbtnmesa3(self,widget, data=None):
        self.lblmesa.set_text("Mesa 3 (4 comensales)")
        self.btnocuparmesa.set_sensitive(True)
        self.btnvaciarmesa.set_sensitive(False)

    def pulsarbtnmesa4(self,widget, data=None):
        self.lblmesa.set_text("Mesa 4 (4 comensales)")
        self.btnocuparmesa.set_sensitive(True)
        self.btnvaciarmesa.set_sensitive(False)

    def pulsarbtnmesa5(self,widget, data=None):
        self.lblmesa.set_text("Mesa 5 (8 comensales)")
        self.btnocuparmesa.set_sensitive(True)
        self.btnvaciarmesa.set_sensitive(False)

    def pulsarbtnmesa6(self,widget, data=None):
        self.lblmesa.set_text("Mesa 6 (8 comensales)")
        self.btnocuparmesa.set_sensitive(True)
        self.btnvaciarmesa.set_sensitive(False)

    def pulsarbtnmesa7(self,widget, data=None):
        self.lblmesa.set_text("Mesa 7 (10 comensales)")
        self.btnocuparmesa.set_sensitive(True)
        self.btnvaciarmesa.set_sensitive(False)

    def pulsarbtnmesa8(self,widget, data=None):
        self.lblmesa.set_text("Mesa 8 (10 comensales)")
        self.btnocuparmesa.set_sensitive(True)
        self.btnvaciarmesa.set_sensitive(False)


    def cambiarestadomesa(self,widget, data=None):
        mesa = self.lblmesa.get_text()
        camarero = self.lblcamarero.get_text()

        if mesa != '' and camarero != '':

            if mesa == "Mesa 1 (4 comensales)":
                self.mesa1.set_from_file("../imagenes/mesa4ocupada.png")
                self.btnmesa1.set_sensitive(False)
                idmesa = 1
                datos.cambiarestadomesa(idmesa)

            if mesa == "Mesa 2 (4 comensales)":
                self.mesa2.set_from_file("../imagenes/mesa4ocupada.png")
                self.btnmesa2.set_sensitive(False)
                idmesa = 2
                datos.cambiarestadomesa(idmesa)

            if mesa == "Mesa 3 (4 comensales)":
                self.mesa3.set_from_file("../imagenes/mesa4ocupada.png")
                self.btnmesa3.set_sensitive(False)
                idmesa = 3
                datos.cambiarestadomesa(idmesa)

            if mesa == "Mesa 4 (4 comensales)":
                self.mesa4.set_from_file("../imagenes/mesa4ocupada.png")
                self.btnmesa4.set_sensitive(False)
                idmesa = 4
                datos.cambiarestadomesa(idmesa)

            if mesa == "Mesa 5 (8 comensales)":
                self.mesa5.set_from_file("../imagenes/mesa8ocupada.png")
                self.btnmesa5.set_sensitive(False)
                idmesa = 5
                datos.cambiarestadomesa(idmesa)

            if mesa == "Mesa 6 (8 comensales)":
                self.mesa6.set_from_file("../imagenes/mesa8ocupada.png")
                self.btnmesa6.set_sensitive(False)
                idmesa = 6
                datos.cambiarestadomesa(idmesa)

            if mesa == "Mesa 7 (10 comensales)":
                self.mesa7.set_from_file("../imagenes/mesa10ocupada.png")
                self.btnmesa7.set_sensitive(False)
                idmesa = 7
                datos.cambiarestadomesa(idmesa)

            if mesa == "Mesa 8 (10 comensales)":
                self.mesa8.set_from_file("../imagenes/mesa10ocupada.png")
                self.btnmesa8.set_sensitive(False)
                idmesa = 8
                datos.cambiarestadomesa(idmesa)

            datos.cargarMesas(self.listmesas,self.treemesas)
            self.limpiarmesas(widget)
        else :
            self.venerror2.show()

    def recuperarmesa(self, widget, data=None):

        model, iter = self.treemesas.get_selection().get_selected()

        if iter != None:
            self.btnocuparmesa.set_sensitive(False)
            self.btnvaciarmesa.set_sensitive(True)

    def vaciarmesa(self,widget, data=None):

        model, iter = self.treemesas.get_selection().get_selected()

        if iter != None:
            id = model.get_value(iter, 0)
            datos.cambiarestadomesavaciar(id)

            if id == 1:
                self.mesa1.set_from_file("../imagenes/mesa4libre.png")
                self.btnmesa1.set_sensitive(True)
                datos.cambiarestadomesavaciar(id)
            if id == 2:
                self.mesa2.set_from_file("../imagenes/mesa4libre.png")
                self.btnmesa2.set_sensitive(True)
                datos.cambiarestadomesavaciar(id)
            if id == 3:
                self.mesa3.set_from_file("../imagenes/mesa4libre.png")
                self.btnmesa3.set_sensitive(True)
                datos.cambiarestadomesavaciar(id)
            if id == 4:
                self.mesa4.set_from_file("../imagenes/mesa4libre.png")
                self.btnmesa4.set_sensitive(True)
                datos.cambiarestadomesavaciar(id)
            if id == 5:
                self.mesa5.set_from_file("../imagenes/mesa8libre.png")
                self.btnmesa5.set_sensitive(True)
                datos.cambiarestadomesavaciar(id)
            if id == 6:
                self.mesa6.set_from_file("../imagenes/mesa8libre.png")
                self.btnmesa6.set_sensitive(True)
                datos.cambiarestadomesavaciar(id)
            if id == 7:
                self.mesa7.set_from_file("../imagenes/mesa10libre.png")
                self.btnmesa7.set_sensitive(True)
                datos.cambiarestadomesavaciar(id)
            if id == 8:
                self.mesa8.set_from_file("../imagenes/mesa10libre.png")
                self.btnmesa8.set_sensitive(True)
                datos.cambiarestadomesavaciar(id)

            self.btnocuparmesa.set_sensitive(True)

        datos.cargarMesas(self.listmesas, self.treemesas)

    def cargarlocalidadescmb (self, widget, data=None):

        self.listlocalidades.clear()
        provincia = self.cmbprovincia.get_active()

        datosprovincias.llenarLocalidades(provincia,self.listlocalidades,self.cmblocalidad)

    def altaCliente (self, widget, data=None):

        dni = self.entdni.get_text().upper()
        apellidos = self.entapellidos.get_text()
        nombre = self.entnombre.get_text()
        direccion = self.entnombre.get_text()

        indexprovincia = self.cmbprovincia.get_active()
        modeloprovincia = self.cmbprovincia.get_model()
        nombreprovincia = modeloprovincia[indexprovincia][0]
        indexlocalidad = self.cmblocalidad.get_active()
        modelolocalidad = self.cmblocalidad.get_model()
        nombrelocalidad = modelolocalidad[indexlocalidad][0]

        if dni != '' and apellidos != '' and nombre != '' and direccion != '' and nombreprovincia != '' and nombrelocalidad != '':
            listadatos = (dni,apellidos,nombre,direccion,nombreprovincia,nombrelocalidad)
            datos.altacliente(listadatos)
            datos.cargarClientes(self.listclientes, self.treeclientes)
            self.limpiarClientes(widget)
            self.cmblocalidad.set_button_sensitivity(False)


    def limpiarcampos(self, widget, data=None):
        panel = self.nbook.get_current_page()

        if panel == 0:
            self.limpiarmesas(widget)
        if panel == 1:
            self.limpiarClientes(widget)



    def limpiarClientes(self, widget, data=None):
        self.entdni.set_text('')
        self.entapellidos.set_text('')
        self.entnombre.set_text('')
        self.entdireccion.set_text('')
        self.cmbprovincia.set_active(-1)
        self.cmblocalidad.set_active(-1)
        self.cmblocalidad.set_button_sensitivity(False)

    def limpiarmesas(self, widget, data=None):
        self.lblmesa.set_text('')


    def recuperarcliente(self, widget, data=None):
        model, iter = self.treeclientes.get_selection().get_selected()


        if iter != None:
            dni = model.get_value(iter, 0)
            apellidos = model.get_value(iter, 1)
            nombre = model.get_value(iter, 2)
            direccion = model.get_value(iter, 3)
            provincia = model.get_value(iter, 4)
            localidad = model.get_value(iter, 5)
            self.entdni.set_text(dni)
            self.entapellidos.set_text(apellidos)
            self.entnombre.set_text(nombre)
            self.entdireccion.set_text(direccion)
            idprovincia = datosprovincias.recuperarprovincia(provincia)
            self.cmbprovincia.set_active(idprovincia)
            self.listlocalidades.clear()
            datosprovincias.llenarLocalidades(idprovincia, self.listlocalidades, self.cmblocalidad)

          #  self.cargarlocalidadescmb()
            idlocalidad = datosprovincias.recuperarlocalidad(localidad,idprovincia+1)
            self.cmblocalidad.set_active(idlocalidad)

    def modificarcliente(self,widget, data=None):

        dni = self.entdni.get_text().upper()
        apellidos = self.entapellidos.get_text()
        nombre = self.entnombre.get_text()
        direccion = self.entnombre.get_text()

        indexprovincia = self.cmbprovincia.get_active()
        modeloprovincia = self.cmbprovincia.get_model()
        nombreprovincia = modeloprovincia[indexprovincia][0]
        indexlocalidad = self.cmblocalidad.get_active()
        modelolocalidad = self.cmblocalidad.get_model()
        nombrelocalidad = modelolocalidad[indexlocalidad][0]


        if dni != '' and apellidos != '' and nombre != '' and direccion != '' and nombreprovincia != '' and nombrelocalidad != '':
            listadatos = (dni, apellidos, nombre, direccion, nombreprovincia, nombrelocalidad)
            datos.modificarCliente(listadatos)
            datos.cargarClientes(self.listclientes, self.treeclientes)
            self.limpiarClientes(widget)
            self.cmblocalidad.set_button_sensitivity(False)





if __name__ == '__main__':
    main = Restaurante()
    Gtk.main()