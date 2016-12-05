#!/usr/bin/env python
#-*-coding: utf-8-*-

print "*** DEĞİŞKEN TANIMI ***"
# Değişken Tanımı
# print x # Hata veriri "NameError: name 'x' is not defined" x tanımıyorum
x = 1
print x
x = "hello world"
print x

print "x"
x= 3
print "y"
y= 5
print "x+y" 
x = x+y
print "x"
print x

print "x**x"
x=x**x
print x

print "y += y"
y += y # = y = y+y
print y

# SWAP iŞlemi
print "swap iŞlemi : "
print "x"
x=2
print "y"
y=3

tmp=x # X'i geçici dosyada tut
x=y
y=tmp # geçici dosyada tuttuğun x değerini y'ye ata
print "x,y,temp"
print x,y,tmp
