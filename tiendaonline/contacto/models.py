# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import EmailValidator
from django.db import models

# Create your models here.
class contact(models.Model):
	nombre= models.CharField(max_length=100)
	email = models.EmailField(blank=False, validators=[EmailValidator(message="Ingresa un email valido")], default='description email')
	comentario = models.TextField(default='description default text')


	def __unicode__(self):
		return self.nombre

class email(models.Model):
	email = models.EmailField(blank=False, validators=[EmailValidator(message="Ingresa un email valido")], default='description email')
	comentario = models.TextField(default='description default text')

	def __unicode__(self):
		return self.email




		

