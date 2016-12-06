#!/usr/bin/env python
#
# Kriptoloji Lab Exercises
#
# Author: Necmettin Çarkacı
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#


from __future__ import division
import  sys
reload(sys)
sys.setdefaultencoding("UTF8")

# Şifreleme_deşifreleme (açık_metin, mod= (şifrele, deşifrele)) ? şifreli_metin
# Texti verilen shift değerine göre şifreler; karakteri shift kadar öteler
# Bu şifreleme yönteminde algoritmanın gizliliği önemlidir. Algoritma ele geçirildiğinde
# deşifreleme işlemi kolayca yapılabilmektedir.
#
def kripto(text, shift_val, mod ):
    # Bir sorun olduğunda text kendisini sonuç olarak döndürüyor
    output = list(text)
    
    for index, harf in enumerate(text):
        if mod == "C":
            output[index] = chr(((ord(harf)+shift_val)%256))
        elif mod == "D":
            output[index] = chr(((ord(harf)-shift_val)%256))
        else:
            print "şifreleme için mod D \nDeşifreleme için mod C kullanınız."
            break
            
    # List objesini string' dönüştür
    output = ''.join(output)

    return output
    
plainText     = "necmeddin"
shiftValue    = 400
encryptedText = kripto(plainText,     shiftValue, mod = "C")
decryptedText = kripto(encryptedText, shiftValue, mod = "D")

# şifreleme_deşifreleme (açık_metin, gizli_anahtar, mod= (şifrele, deşifrele)) ? şifreli_metin
# Anahtar kullarak şifreleme ve deşifreleme yapar.
# Anahtar shift value hesaplamak için kullanılır
# Shift val hesaplanırken anahtardaki her bir karakter toplanarak tek bir integer değer elde edilir.
# Parametre olarak shift value yerine anahtar kullanılıyor ve şifreleme için ilk kripto fonksiyonunu çağırıyor
# kripto algoritmasına benzer şekilde bu yöntemde gizli anahtar kullanılmış olmasına rağmen algoritmanın
# gizliliği önemlidir, çünkü anahtardan üretilen shift değeri tüm xor işlemleri için sabit olacaktır ve maksimum
# 256 karakterlik bir kümenin elamanı olacaktır
#
def kripto_anahtar(anahtar, text, mod ):
    
    shift_val = 0 # Anahtar yoksa metnin kendisini geri döndür
    
    # Anahtardan shift_val hesapla
    for char in anahtar:
        shift_val = shift_val+ord(char)
    print "Anahtar Shift Değeri : "+str(shift_val)
        
    return kripto(text,int(shift_val),mod)

anahtar       = "anahtar"
plainText     = "necmeddin"
encryptedText = kripto_anahtar(anahtar, plainText,      mod = "C")
decryptedText = kripto_anahtar(anahtar, encryptedText,  mod = "D")