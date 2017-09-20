# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Catalogo

class profileAdmin(admin.ModelAdmin):
    class Meta:
        model = Catalogo

admin.site.register(Catalogo, profileAdmin)