"""tiendaonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django_pdfkit import PDFView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from contacto import views as contact_views
from profiles import views as profiles_views
from producto import views
from catalogo import views
from servicios import views as servicios_views

#URLS necesarias para la aplicacion
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^contacto/$', contact_views.contacto, name='contacto'),
    url(r'^servicios/$', servicios_views.Servicios, name='servicios'),
    url(r'^$', profiles_views.home, name='home'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^reporte/$', servicios_views.Reporte, name='reporte_pdf'),
    #url(r'^reporte/$', PDFView.as_view(template_name='pdf_template.html'), name='reporte_pdf'),
    url(r'^email/$', contact_views.email, name='email')

]


if settings.DEBUG:
	urlpatterns == static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
	urlpatterns == static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
