#!/usr/bin/env python
#
# DES Simetrik Şifreleme algoritması üzerinden çığ etkisi gösterilmesi
# Author: Necmettin Çarkacı
# E-mail: necmettin [ . ] carkaci [ @ ] gmail [ . ] com
#
#Usage : avalanche_affects.py

from Crypto.Cipher import DES


def avalancheAffectAnaysisOnDES(key, plaintext) :
	'''
		Kriptoloji de kullanılan çığ etkisinin des ve aes şifreleme algoritmaları
	üzerinden incelemesi yapılmaktadır. Açık metinde meydana gelen tek karakterlik bir değişim
	şifreli metnin en az %50'sini değiştirmesi beklenmektedir.

		@inspiration Mehmet İnce Blog yazısından ilhamla oluşturuldu.
		@url https://www.mehmetince.net/crypto-101-2-block-cipher-encryption-ve-des-analizi/

		@ param key       	: <string> Şifreleme algoritmasında kullanılacak anahtar
		@ param plaintext 	: <string> Şifrelenecek metin 

		@ return 			: <void>
	''' 

	des = DES.new(key, DES.MODE_ECB)
	cipher_text = des.encrypt(plaintext)

	print ("Açık Metin : "+plaintext)
	print ("Açık Metin (Hex Code)   = {0}".format(repr(cipher_text)))

	# Cipher text is = '\x85\x94<z\x11H\xee\x00*\xd4\x0eC\xd6\xbf\xf9b'
	changed_text = b'\x85\x94<z\x11h\xee\x00*\xd4\x0eC\xd6\xbf\xf9b'

	print ("Tek karakter değişmiş metin = {0}".format(repr(changed_text)))
	print ("Orjinal metin için deşifreleme  = {0}".format(des.decrypt(cipher_text)))
	print ("Değiştirilmiş metin için deşifreleme  = {0}".format(des.decrypt(changed_text)))


if __name__ == '__main__':

	key = "g1zl1KEY" # Sekiz byte olmalı
	plaintext = "gizli-bilgi-lab-" # 8 Katları şeklinde olmalı
	avalancheAffectAnaysisOnDES(key, plaintext)

