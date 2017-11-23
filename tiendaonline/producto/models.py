# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Producto(models.Model):
	nombre = models.CharField(max_length=300)
	descripcion = models.TextField()
	precio = models.DecimalField(max_digits=20, decimal_places=2)

	def __unicode__(self):
		return self.nombre
