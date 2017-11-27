# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from producto.models import Producto

# Create your views here.
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.pagesizes import A4, cm

from django.template.loader import get_template
from django.template import Context
#from weasyprint import HTML, CSS
import pdfkit
#from markdown import markdown
from django.http import HttpResponse


def Reporte(request):

    product= Producto.objects.all()
    #Indicamos el tipo de contenido a devolver, en este caso un pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename= reporte-lab.pdf'
    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utilizacomo almacenamiento temporal
    buffer = BytesIO()
    #Canvas nos permite hacer el reporte con coordenadas X y Y
    pdf = canvas.Canvas(buffer, pagesize= A4)

    #Cabecera del reporte
    logo=ImageReader('https://cdn6.aptoide.com/imgs/4/5/a/45a6b5cdb2a4e4c51ba127f15427adf6_icon.png?w=60')
    pdf.drawImage(logo, 50,770, mask='auto')
    pdf.drawString(30, 750, 'SEXSHOP CEREZAPP')
    pdf.drawString(30, 730, 'Reporte Productos')

    #Cuerpo del reporte
    n = 300
    for ae in product:
            pdf.drawString(30, n, ae.nombre)
            pdf.drawString(200, n, ae.descripcion)
            pdf.drawString(500, n, str(ae.precio))
            n+=20



    pdf.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

    #html_template = get_template('/pdf_template.html')

    #template = get_template("servicios.html")
    #context = Context({"data": data})  # data is the context data that is sent to the html file to render the output.
    #html = template.render(context)  # Renders the template with the context data.
    #pdfkit.from_string(html, 'Reporte_productos.pdf')
    #pdf = open("Reporte_productos.pdf")
    #response = HttpResponse(pdf.read(), content_type='application/pdf')  # Generates the response as pdf response.
    #response['Content-Disposition'] = 'attachment; filename=Reporte_productos.pdf'
    #pdf.close()
    #os.remove("Reporte_productos.pdf")  # remove the locally created pdf file.
    #return response  # returns the response.

    #response = HttpResponse(pdf_file, content_type='application/pdf')
    #response['Content-Disposition'] = 'filename="Reporte_productos.pdf"'
    #return response

    #HTML a PDF con WeasyPrint
    #html_template = get_template('/pdf_template.html')
    #pdf_file = HTML(string=html_template).write_pdf()
    #response = HttpResponse(pdf_file, content_type='application/pdf')
    #response['Content-Disposition'] = 'filename="Reporte_productos.pdf"'
    #return response

def Servicios(request):
    title='Lista de Productos'
    product= Producto.objects.all()
    context={
    	'title': title, 'listaproductos':product,
    }
    print product

    template = 'servicios\servicios.html'
    return render(request,template, context)
