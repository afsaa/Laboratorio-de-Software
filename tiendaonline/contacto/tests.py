# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from contacto.forms import contactForm
from django.test import TestCase
from contacto.models import contact


# Create your tests here.
class Testcontacto(TestCase):
    def test_contact_str(self):
        mycontact = contact(nombre='Chérer')
        self.assertEqual(str(mycontact), 'Chérer'.encode('utf8'))

    def test_contact_str1(self):
        mycontact = contact(nombre='fa21ere')
        self.assertEqual(str(mycontact), 'Chaarri'.encode('utf8'))

    def test_contact_str2(self):
        mycontact = contact(nombre='fa21ere')
        self.assertEqual(str(mycontact), contact.nombre)

    def test_contact_str3(self):
    	contact.objects.create(nombre="haloe")
        mycontact = contact(nombre='haloe')        
        self.assertEqual(str(mycontact), "haloe") 

    def test_unique_together_validation_should_work_for_person(self):
        data = contactForm({'email':'Norris@gmail.com'})
        self.assertFalse(data.is_valid())

    def test_email_used_by_django_auth_is_invalid(self):
        form = contactForm({'email': 'les@example.org'})
        self.assertFalse(form.is_valid())

    def test_email_used_by_django_auth_is_invalid1(self):
        form = contactForm({'email': 'lesre@xample.org'})
        self.assertFalse(form.is_valid())    
                   
