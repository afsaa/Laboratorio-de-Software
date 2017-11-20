# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from producto.models import Producto

def Servicios(request):
	title='Lista de Productos'
	product= Producto.objects.all()
	context={
		'title': title, 'listaproductos':product, 
	}
	print product
	
	template = 'Servicios\servicios.html'
	return render(request,template, context)