#!/usr/bin/env python
#-*-coding: utf-8-*-



# FONKSÝYON TANIMLAMA
print "*** FONKSÝYON TANIMLAMA ***"
def fonkA():
    print "Ben A fonksiyonum"

fonkA() # fonksiyonu çaðýralým

def fonkB():
    print "Ben B fonksiyonum. Þimdi A fonksiyonunu çaðýracaðým"

fonkB()


# parametre alan fonksiyon aldýðý paramtreyi ekrana yazýyor
def fonk2(param):
	print param

# fonksiyonu çaðýralim
fonk2("deneme parametresi bakalým ne olacak ")

#birden fazla paramtre alan fonksiyon
def fonk3(param, param2):
	print param
	print param2
	print param+param2
        
        
#fonksiyonu çaðýralým
fonk3("parametre 1 ","parametre 2 ")


# ekrandan metin alýp aldýðý metni tekrar ekrana yazan fonksiyon
def ekranaYamaFonksiyonu():
    data =  raw_input("Ekran yazýlacak metni girin. Çýkýþ içi q yazýn : ")
    
    if data == "q":
        print "Çýkýyorum ..."
        exit
    else:
        print data
        ekranaYamaFonksiyonu()

# fonksiyonu çalýþtýralým
ekranaYamaFonksiyonu()
    
def dort_islem(param1, param2, islemkod):
	
        if islemkod=="+":
            return param1+param2
        elif islemkod == "*":
            return param1*param2
        elif islemkod == "/":
            return param1/param2
        elif islemkod == "%":
            return param1%param2
        elif islemkod == "-":
            return param1-param2
        else:
            print "Ýþlem Kod Tanýnamadý : "+islemkod

dort_islem(3, 5, "%")

# Biz çýkana kadar ekrandan iþlem yapan bir program 
def dort_islem_ekrandan():
    sayi1 = raw_input("Sayý Giriniz : ")
    sayi2 = raw_input("Sayi Giriniz : ")
    islemkod = raw_input("Yapýlacak Ýþlem Türünü Giriniz (Çýkýþ Ýþlemi için q yazýnýz ): ")
    
    if islemkod == "q":
        print "Çýkýyorum ..."
        exit
    else: 
        print dort_islem(int(sayi1), int(sayi2), islemkod)
        dort_islem_ekrandan()
    

dort_islem_ekrandan()

def asalmi(asal_sayi):
    for sayi in range(2,asal_sayi):
        if(asal_sayi%sayi) == 0:
            return False
    return True

print asalmi(4)

    
def asal_sayilar(limit):
    for sayi in range(1,limit):
        if asalmi(sayi):
            print sayi


asal_sayilar(20)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
 

var1 = factorial(4)
var2 = factorial(100)

print var1
print var2

def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)

print fibonacci(5)

def pritnAllFibonacciNum(n):
    print "Fibonacci Sayýlarýný Sýralýyorum : "
    print "Sýra : "+"   Deðer : "
    for sayi in range (0,n):
        print sayi,fibonacci(sayi)
        
pritnAllFibonacciNum(6)
