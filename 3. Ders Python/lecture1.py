#!/usr/bin/env python
#-*-coding: utf-8-*-
#Bu bir türkçe karakterli yorum satırıdır. Eðer sayfanın başına "encoding utf-8" satırını 
# eklemezseniz "SyntaxError: Non-ASCII character" hatası verecektir.

import math # math kütüphanesini import eder


print "Hello world" # Ekrana metin yazar. Tırnak işareti kullanmazsan hata verir

print "*** MATEMATıKSEL ışLEMLER ***"
# Basit matematiksel işlemler
print 1 # Ekranan sayı yazar
print "Toplama sonucu :"
print 1+2 # Ekrana toplama işlemnin sonucunu yazar
print "Çıkarma sonucu : "
print 4-7 # Ekrana çıkarma işlemnin sonucunu basar
print "Çarpma sonucu : "
print 2*3 # Ekrana çarpım işlemnin sonucunu yazar
print "Üs alma sonucu"
print 2**3 # ekranan sayının üssü alır sonucu yazar
print "Bölme sonucu : "
print 5/2 # Ekranan bölme işlemi sonucu yazar
#print 1/0 # Division hatası verir
print "Kalan sonucu :"
print 10%3 # Ekrana bölme işleminin kalanını basar
print "Max bulma sonucu : "
print max(3,8,1,10,5)
print "Min bulma sonucu : "
print min(3,8,1,10,5)

# Math kütüphane fonksiyonları ile matematiksel işlemler
#print sin(30) # 'sin' is not defined hatası veriri çünkü math kütüphanesinin bir fonksiyonudur
print "sinus sonucu : "
print math.sin(30) # Neden farklı sonuç verdi
print "Kök sonucu : "
print math.sqrt(4) # Sayının karekökünü ekrana basar
