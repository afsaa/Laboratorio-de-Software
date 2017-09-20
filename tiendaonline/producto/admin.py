# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Producto

class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = Producto

admin.site.register(Producto, profileAdmin)