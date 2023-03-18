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
Desktop  Documents  Downloads  yeni_dizin  yeni_dosya.txt

```

**cp komutu**: Bu komut, belirtilen dosyayı veya dizini kopyalar.

```bash
$ cp yeni_dosya.txt yeni_dosya2.txt
$ ls
Desktop  Documents  Downloads  yeni_dizin  yeni_dosya.txt  yeni_dosya2.txt
```

**rm komutu**: Bu komut, belirtilen dosyayı veya dizini siler.

```bash
$ rm yeni_dosya2.txt
$ ls
Desktop  Documents  Downloads  yeni_dizin  yeni_dosya.txt
```

**find komutu**: belirtilen bir dizinde ve alt dizinlerinde arama yapmak için kullanılan bir Linux komutudur. Arama sonuçları, belirtilen arama kriterlerine göre filtrelenir ve ekrana yazdırılır.

<pre class="language-bash"><code class="lang-bash"><strong>$ find /home -name "*.txt"
</strong>/home/user/Documents/example.txt
/home/user/Desktop/test.txt
/home/user/Downloads/report.txt
</code></pre>

Bu örnekte, "/home" dizininde üç farklı klasörde ".txt" uzantılı dosyalar bulunmuştur ve find komutu tarafından bu dosyaların tam yolları ekrana yazdırılmıştır.Bash

**ps komutu**: Bu komut, çalışan işlemleri listeler.

```bash
$ ps
  PID TTY          TIME CMD
 1234 pts/0    00:00:00 bash
 5678 pts/0    00:00:00 ps
```

**kill komutu**: Bu komut, belirtilen PID numarasına sahip işlemi sonlandırır.

```bash
$ kill 1234h
```

**top komutu**: Linux/Unix sistemlerinde sistem kaynaklarını izlemek için kullanılan bir araçtır. Bu komut, sistemin CPU kullanımı, bellek kullanımı, işlem sayısı ve diğer kaynak kullanım istatistiklerini gösterir.

```bash
top - 12:55:35 up 10 days, 17:32,  2 users,  load average: 0.00, 0.01, 0.05
Tasks: 139 total,   1 running,  87 sleeping,   0 stopped,   1 zombie
%Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :  15859.7 total,   1116.7 free,  11245.7 used,   3476.7 buff/cache
MiB Swap:  16384.0 total,  15738.8 free,    645.2 used.   3356.7 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
 3526 john      20   0 2478208 678476  63500 S   0.0   4.2   4:15.50 firefox
 1083 root      20   0       0      0      0 Z   0.0   0.0   0:00.00 zombie
  890 mysql     20   0 1552776 273952  25364 S   0.0   1.7  23:18.43 mysqld
  726 root      20   0   30572   6248   5152 S   0.0   0.0  22:33.19 systemd-journal
  772 root      20   0  243900   5708   3908 S   0.0   0.0  18:44.70 NetworkManager
 2911 john      20   0  908776 147840  90044 S   0.0   0.9   0:01.57 gnome-terminal-
 2364 john      20   0 1449552  34812  26156 S   0.0   0.2   0:09.60 gvfsd-http

```

Yukarıda, PID 1083'e sahip bir zombi işlemi var. Bu işlem, hafızada herhangi bir yer kaplamaz, ancak hala sistem kaynaklarını kullanabilir ve ebeveyn süreci tarafından sonlandırılmayı bekleyebilir.
