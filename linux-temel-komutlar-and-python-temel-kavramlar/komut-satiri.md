---
description: Linux Shell Nedir ve Nasıl Çalışır?
cover: >-
  https://images.unsplash.com/photo-1629654297299-c8506221ca97?crop=entropy&cs=tinysrgb&fm=jpg&ixid=MnwxOTcwMjR8MHwxfHNlYXJjaHwzfHxsaW51eCUyMHRlcm1pbmFsfGVufDB8fHx8MTY3OTAxODY4Nw&ixlib=rb-4.0.3&q=80
coverY: -23
---

# Komut Satırı

Linux Shell, kullanıcının komutları yazdığı ve çalıştırdığı bir komut yorumlayıcısıdır. Shell, kullanıcı ile işletim sistemi arasında bir arayüz görevi görür ve komutları kabul eder, yorumlar ve sonuçlarını kullanıcıya geri döndürür.

Birçok farklı Linux kabuğu mevcuttur, ancak en yaygın olanı Bash (Bourne-Again SHell)'tir. Bash, UNIX'teki orijinal Bourne Shell'in bir geliştirmesi olarak ortaya çıktı ve Linux için standart kabuk olarak kullanılıyor.

Kullanıcılar, kabukta bir komut yazarken veya çalıştırırken birçok farklı işlem yapabilirler. Bazı örnekler şunlardır:

* Dosya sistemini gezinme
* Dosya ve dizinleri oluşturma, kopyalama, taşıma ve silme
* Dosya içeriği okuma ve yazma
* Dosyaları ve dizinleri arama ve sıralama
* Programları çalıştırma ve durdurma
* Sistem ayarlarını ve ortam değişkenlerini ayarlama

**ls komutu**: Bu komut, mevcut dizindeki dosya ve klasörleri listeler.

```bash
$ ls
Desktop  Documents  Downloadsbash
```

```bash
$ ls -la
total 64
drwxr-xr-x  16 user  staff   512 Mar 17 11:44 .
drwxr-xr-x  18 user  staff   576 Mar 17 10:47 ..
-rw-r--r--   1 user  staff     0 Mar 17 11:23 .file1
-rw-r--r--   1 user  staff     0 Mar 17 11:23 .file2
drwxr-xr-x   4 user  staff   128 Mar 17 11:36 folder1
drwxr-xr-x   4 user  staff   128 Mar 17 11:44 folder2
-rw-r--r--   1 user  staff  1656 Mar 17 11:23 index.html
-rw-r--r--   1 user  staff     0 Mar 17 11:23 script.js

```

**cd komutu**: Bu komut, belirtilen dizine geçiş yapar.

```bash
$ cd Documents/
$ pwd
/home/user/Documents
```

**mkdir komutu**: Bu komut, belirtilen isimde bir dizin oluşturur.

```bash
$ mkdir yeni_dizin
$ ls
Desktop  Documents  Downloads yeni_dizin
```

**touch komutu**: Bu komut, belirtilen isimde bir dosya oluşturur.

```bash
$ touch yeni_dosya.txt
$ ls
Desktop  Documents  Downloads yeni_dizin  yeni_dosya.txt

```
