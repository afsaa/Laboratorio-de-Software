# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
from django.db import models

# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length=120)
	description = models.TextField(default='description default text')	
	regla_telefono = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El formato de telefono es: '+999999999'. maximo 15 digitos permitido.")
	telefono = models.CharField(validators=[regla_telefono], max_length=15, blank=True)
	email = models.EmailField(blank=False, validators=[EmailValidator(message="Ingresa un email valido")], default='description email')
	direccion = models.CharField(max_length=120, default='description address text')

	def __unicode__(self):
		return self.name
