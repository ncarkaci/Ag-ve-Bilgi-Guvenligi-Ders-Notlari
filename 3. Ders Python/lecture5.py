#!/usr/bin/env python
#-*-coding: utf-8-*-


print "*** DOSYA OKUMA YAZMA ***"

# Dosyayý aç
file = open("deneme.txt","a+")

string1 = "metin 1 "
string2 = "metin 2 "
string3 = "metin 3 ve diðerleri "+string1+string2

# Dosyaya yaz
file.write(string1)
file.write(string2)
file.write(string3)
file.close() # Dosyayý kapat

# Dposyayý aç
file = open("deneme.txt","r")
print file # Size dosyanýn içeriðini vermez, dosyanýn durumunu verir : "<open file 'deneme.txt', mode 'r' at 0x00000000021B4150>" sonucu verir.

# Dosyanýn içeriðini iki þekilde okuyabilirsiniz 
# 1. Durum
f = file.read() # Dosyayý read fonksiyonuyla oku ve bir deðiþkenen ata daha sonra o deðiþkeni print et
print f+"\n"

# 2. Durum dosyayý for döngüsüyle oku ve her satýrý ekrana bas
for satir in file: # Satýr satýr dosyayý oku
    print satir

# Dosyanýn içindeki metinleri harf harf okumak için bu ikisini birleþtirelim

for satir in f:
    print satir
    
# Konsoldan veri okuyup dosyay yazalým

data =  raw_input("Lütfen dosyay yazýlacak metni giriniz : ")

file = open("deneme.txt","a+")

file.writelines(data)
for satir in file:
    print satir
