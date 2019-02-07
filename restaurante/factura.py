from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os
import sqlite3
import locale

try:
    bbdd = 'restaurante'
    conexion = sqlite3.connect(bbdd)
    cur = conexion.cursor()
    print('BASE DE DATOS CONECTADA')

except sqlite3.OperationalError as e:
    print(e)


def cerrarConexion():
    try:
        conexion.commit()
        conexion.close()
        print('cerrando base de datos')
    except sqlite3.OperationalError as e:
        print(e)

def cabecera(cser,idfactura, dnicliente):

    try:
        cser.setTitle('Informes')
        cser.setAuthor('Daniel Bastos Rodriguez')
        cser.setFont('Helvetica', 11)

        cser.line(50, 820, 545, 820)
        cser.line(50, 720, 545, 720)
        cser.line(50, 700, 545, 700)
        textnom = 'Restaurante Atracón'
        textdir = 'Calle False 123- Springfield'
        texttlfo = '666 66 66 66'
        cser.drawCentredString(297.5, 795, textnom)
        cser.drawCentredString(297.5, 775, textdir)
        cser.drawCentredString(297.5, 755, texttlfo)
        cur.execute("select Nombre from Camarero c, Factura f where f.Idfactura = ? and c.Idcamarero = f.Idcamarero",
                    (idfactura,))
        camarero = cur.fetchall()
        conexion.commit()
        cser.drawString(450, 745, "Le atendió: " + camarero[0][0])
        cser.drawString(450, 730, "Cliente: " + dnicliente)



    except:
        print ('erros cabecera')

def pie(cser):
    try:
        cser.line(50, 20, 525, 20)
        textgracias = "Gracias por su visita - Vuelva pronto"
        cser.drawCentredString(297.5, 10, textgracias)

    except:
        print('erros pie')


def crearfactura(idfactura,dnicliente):
    try:
        cser = canvas.Canvas(str(idfactura) + '.pdf', pagesize=A4)

        cabecera(cser,idfactura,dnicliente)
        pie(cser)
        cur.execute("select l.Idventa, p.Nombreproducto, l.Cantidad, p.Preciounidad from Lineafactura l, Producto p "
                    "where l.Idfactura = ? and p.Idproducto = l.Idproducto", (idfactura,))
        listado = cur.fetchall()
        conexion.commit()

        textlistado = 'Cod       Concepto                              Unidades                        Precio/unidad                                  Total'
        cser.drawString(50, 705, textlistado)
        cser.line(50, 700, 545, 700)
        x = 50
        y = 680
        total = 0
        for registro in listado:
            for i in range(4):
                if i <= 1:
                    cser.drawString(x, y, str(registro[i]))
                    x = x + 40
                else:
                    x = x + 120
                    cser.drawString(x, y, str(registro[i]))


                var1 = int(registro[2])
                var2 = registro[3]
                var2 = var2
                var2 = round(float(var2), 2)
                subtotal = var1*var2
            total = total + subtotal
            subtotal = locale.currency(subtotal)
            x = x + 120
            cser.drawRightString(545, y, str(subtotal))
            y = y - 20
            x = 50
        y = y -20
        cser.line(50, y, 545, y)
        y = y -20
        x = 400
        cser.drawString(x, y, 'Total: ')
        x = 485
        total = round(float(total), 2)
        total = locale.currency(total)
        cser.drawString(x,y,str(total))
        cser.showPage()
        cser.save()
        dir = os.getcwd()
        os.system('/usr/bin/xdg-open ' + dir + '/' + str(idfactura) + '.pdf')


    except sqlite3.OperationalError as e:
        print(e)
        conexion.rollback()
        print('error en factura')