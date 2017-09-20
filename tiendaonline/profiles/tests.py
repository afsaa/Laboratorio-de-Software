# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from profiles.models import profile

# Create your tests here.
class TestProfiles(TestCase):
    def test_myperfil_str(self):
        myperfil = profile(name='Chéri')
        self.assertEqual(str(myperfil), 'Chéri'.encode('utf8'))

    def test_myperfil_str2(self):
        myperfil = profile(name='fa21er')
        self.assertEqual(str(myperfil), 'Chéri'.encode('utf8'))

    def test_myperfil_str3(self):
        myperfil = profile(name='fa21er')
        self.assertEqual(str(myperfil), profile.name)

    def test_myperfil_str4(self):
    	profile.objects.create(name="heynow")
        myperfil = profile(name='heynow')
        self.assertEqual(str(myperfil), "heynow")             


    def test_myperfil_telefono(self):
        myperfil = profile(telefono='3113032015')
        self.assertTrue(True)

        myperfil2 = profile(telefono='+3158889498')
        self.assertEqual(myperfil2, myperfil)  

    

   

