#!/usr/bin/env python
#-*-coding: utf-8-*-


print "*** KONSOLDAN DEÐER ALMA ***"
# Kullanýcýdan deðer alma iþlemi
print "Kullanýcýdan deðer alma : "
ad    = raw_input('Ad : ')
soyad = raw_input('Soyad : ')

print ad, soyad
print "Ad : "+ad+" Soyad : "+ soyad
print "Büyük harfe dönüþtür"
print "Ad : "+ad.upper()+" Soyad : "+ soyad.upper()

# CONDITIONS
print "*** CONDITIONS ***"
# if condition
print "if conditions"
# Boþluk intend kavramý ve hatalar
if 3>2:
    print "if doðru olduðunda"
else:
    print "else yanlýþ olduðu durum"
    
x = 3
y = 9

if x > y:
    print "x y'den büyük"
else:
    print "y x^den büyük"
    
print "Mantýksal operatörler"
#  < > <= >= == != her biri için if örneði yapalým, özellikle == ve = farký
# Önemli assigment iþlemi ve eþitlik kontrolü
#  && || !

ad    = raw_input('X deðeri giriniz : ')
soyad = raw_input('Y deðeri giriniz : ')

if x > y:
    print "x y'den büyük"
else:
    print "y x^den büyük"
    
