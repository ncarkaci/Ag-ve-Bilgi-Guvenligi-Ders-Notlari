#!/usr/bin/env python
#
# Kriptoloji Dizi Şifreleme Uygulaması
#
# Author: Necmettin Çarkacı
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#


from __future__ import division
import  sys
reload(sys)
sys.setdefaultencoding("UTF8")

# Anahtar ile birebir şifreleme
# Anahtar ile metin birebir eşlenir;
# Bu algoritmada anahtar yanyana yazılmışçasına metnin herbir karakterini şifreler
# Bu algoritmanın zayıf tarafı anahtar boyutunun küçük olduğu durumlarda birbirini
# tekrarlayan şifreleme durumlarının oluşmasıdır. Bu algoritma için en çözüm 
# metin uzunluğunca anahtar kullanılmasıdır. Bu yöntemle birlikte algoritmanın gizli
# tutulması sorunu ortadan kaldırılmıştır; algoritmanın ele geçirilmesi doğrudan 
# şifrenin çözülmesine neden olmayacaktır. Bununla birlikte; bu durum anahtar dağıtım sorununu
# ortaya çıkarmaktadır. Büyük boyutlu gizli anahatarlar nasıl paylaşılacaktır.
# 
def kripto_anahtar_birebir_sifreleme(anahtar, text, mod):
    
    output = list(text) # Bir sorun olduğunda text kendisini sonuç olarak döndürüyor
    
    for index, harf in enumerate(text):
        
        # Anahtar metnin uzunluğunca yanyana yazılarak, metin uzunluğunda bir anahtar elde edilir
        anahtar_index = index%len(anahtar)
        anahtar_harf  = anahtar[anahtar_index:anahtar_index+1]
        
        if mod == "C":
            output[index] = chr(((ord(harf)+ord(anahtar_harf))%256))
        elif mod == "D":
            output[index] = chr(((ord(harf)-ord(anahtar_harf))%256))
        else:
            print "şifreleme için mod D \nDeşifreleme için mod C kullanınız."
            break
            
    # List objesini string' dönüştür
    output = ''.join(output)

    return output

anahtar       = "anahtar"
plainText     = "necmeddin"
encryptedText = kripto_anahtar_birebir_sifreleme(anahtar, plainText,      mod = "C")
decryptedText = kripto_anahtar_birebir_sifreleme(anahtar, encryptedText,  mod = "D")


#Anahtar_dizisi_üret (gizli_anahtar, kayan_anahtar_dizisi_boyu) ? kayan_anahtar_dizisi 
# Verilen anahtarı kullanarak kayan anahtar dizisi üretir;
# Yani verilen anahtardan teorik olarak birbirini tekrarlamayacak şekilde plaintext
# boyutunda anahtar üretir. 
# Bununla birlikte char 256 karakter sınırında olduğundan en fazla 256 farklı karakter kümesinde
# çalışabilecektir ki bu durum çakışmaya neden olabilecektir.
# 
def kayan_anahtar_dizisi_uret(gizli_anahtar,kayan_anahtar_dizi_boyutu):
    
    output = list()
    for index in range(0,kayan_anahtar_dizi_boyutu):
        
        str_index    = index%len(gizli_anahtar)
        anahtar_harf = gizli_anahtar[str_index:str_index+1]
        output.append(chr(((ord(anahtar_harf)+index)%256)))

    output = ''.join(output)
    print "Kayan Anahtar Dizisi : "+output
    return output

anahtar                 = "anahtar"
plainText               = "necmeddin"
kayanAnahtarDiziBoyu    = len(plainText)# Anahtar dizisi boyutu şifrelenecek metnin boyutuyla eşdeğerdir
kayan_anahtar_dizisi    = kayan_anahtar_dizisi_uret(anahtar,kayanAnahtarDiziBoyu)

# Dizi şifreleme gizli anahtardan oluşturulan açık metin boyutundaki anahtarı
# kullanarak birebir şifreleme yapan algoritmadır
# Bu yöntem birebir şifreleme için küçük boyutlu anahtarların oluşturduğu çakışma
# problemine çözüm üretmiştir. Bununla birlikte, şifrelemede dizi boyutunda anahtar
# kullanılması şifreleme işlemini yavaşlatacaktır. Kayan dizinin tek bir anahatar
# ile oluşturulması kayan dizinin oluşturulmasına yönelik saldırılarda başarı düzeyini etkileyecektir
#
def dizi_sifreleme(anahtar, text, mod):
    kayan_anahtar = kayan_anahtar_dizisi_uret(anahtar, len(text))
    return kripto_anahtar_birebir_sifreleme(kayan_anahtar, text, mod)


anahtar                 = "anahtar"
plainText               = "necmeddin"
encryptedText           = dizi_sifreleme(anahtar, plainText,     mod="C")
decryptedText           = dizi_sifreleme(anahtar, encryptedText, mod="C")
    