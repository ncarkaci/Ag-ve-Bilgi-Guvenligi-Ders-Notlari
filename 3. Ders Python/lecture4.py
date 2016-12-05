#!/usr/bin/env python
#-*-coding: utf-8-*-


print "*** FOR LOOP *** "

for number in range(3, 6):
    print number

x = 3
y = 10

for number in range(x, y):
    print number

print "while iþlemi : "
number = 3
while(number < 6):
    print number
    number = number+1 # while iþlemini döngüden kurtarýr, base step oluþturur onun için

print "*** STRINGLER ***"
"bu bir stringdir"

stringdegiskeni = "deneme"
# deðiþkenin her harfini ekrana bas
for harf in stringdegiskeni:
    print harf

# Kullanýcýdan string al ve her harfi ekrana bas
stringdegiskeni = raw_input("herhangi bir metin gir : ")
for harf in stringdegiskeni:
    print harf


print "String birlþetirme : "
string1 = "deneme1"
string2 = "deneme2"
string3 = string1+string2
print string1, string2, string3

print "Substring iþlemleri : "
print string3[0], string3[5], string3[2:5], string3[5:], string3[:5]


print "string boyu : "
print len(string3)


