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