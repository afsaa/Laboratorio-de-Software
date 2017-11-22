# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from producto.models import Producto

# Create your views here.
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, cm

from django.http import HttpResponse


def Reporte(request):

    #Indicamos el tipo de contenido a devolver, en este caso un pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename= reporte-lab.pdf'
    #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utilizacomo almacenamiento temporal
    buffer = BytesIO()
    #Canvas nos permite hacer el reporte con coordenadas X y Y
    pdf = canvas.Canvas(buffer, pagesize= A4)

    #Cabecera
    pdf.drawString(30, 750, 'Reporte')
    pdf.drawString(30, 735, 'Laboratorio')

    pdf.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def Servicios(request):
	title='Lista de Productos'
	product= Producto.objects.all()
	context={
		'title': title, 'listaproductos':product,
	}
	print product

	template = 'servicios\servicios.html'
	return render(request,template, context)
