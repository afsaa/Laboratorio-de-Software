# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Catalogo(models.Model):
	nombre_catalogo = models.CharField(max_length=255)
	descripcion = models.TextField()
	fecha_publicacion = models.DateTimeField(auto_now_add=True, blank=True)

	def __unicode__(self):
		return self.nombre_catalogo
