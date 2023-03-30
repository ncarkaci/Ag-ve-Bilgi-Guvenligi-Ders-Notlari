---
cover: >-
  https://images.unsplash.com/photo-1639262498805-17c7dc422d37?crop=entropy&cs=tinysrgb&fm=jpg&ixid=MnwxOTcwMjR8MHwxfHNlYXJjaHw5fHxtYXRyaXh8ZW58MHx8fHwxNjc5MTk3NDA4&ixlib=rb-4.0.3&q=80
coverY: 0
---

# 🚀 Uygulama : Mors alfabesi

### AMAÇ :

Bu uygulamanın amacı, kişilere Morse alfabesi kullanarak, alfabedeki harflerin farklı bir uzayda temsil edilmesi konusunda örnekler sunmaktır.

### ÖNBİLGİ :

Morse alfabesi veya Morse kodu, bilgi iletimi için kısa ve uzun işaretlerin (• ve –) ve bu işaretlere karşılık gelen ışık veya seslerin kullanıldığı bir yöntemdir. Bu yöntem, Samuel Morse tarafından 1835 yılında telgrafın geliştirilmesiyle birlikte oluşturuldu ve 1837'de kullanılmaya başlandı. Morse kodu, sesli olarak, radyo sinyallerinin açılıp kapatılmasıyla, telegraf tellerinden geçen elektrik akımıyla, mekanik yolla veya görsel olarak (ışıkların yanıp sönmesi gibi) çeşitli yollarla iletilir.

### UYGULAMA ÖNCESİ:

* `sudo apt-get install audacity` komutuyla ses uygulamasını kurun

### UYGULAMA:

**Tablo 1: Mors Alfabesi Harf Kod Tablosu**

| **Harf** | **Kod**    | **Karakter** | **Kod**          |
| -------- | ---------- | ------------ | ---------------- |
| Aa       | · −        | .            | · − · − · −      |
| Bb       | − · · ·    | ,            | − − · · − −      |
| Cc       | − · − ·    | ?            | · · − − · ·      |
| Çç       | − · − · ·  | ‚            | · − − − − ·      |
| Dd       | − · ·      | !            | − · − · − −      |
| Ee       | ·          | /            | − · · − ·        |
| Ff       | · · − ·    | (            | − · − − ·        |
| Gg       | − − ·      | )            | − · − − · −      |
| Ğğ       | − − · − ·  | :            | − − − · · ·      |
| Hh       | · · · ·    | ;            | − · − · − ·      |
| Ii       | · ·        | =            | − · · · −        |
| Jj       | · − − −    | +            | · − · − ·        |
| Kk       | − · −      | -            | − · · · · −      |
| Ll       | · − · ·    | \_           | · · − − · −      |
| Mm       | − −        | “            | · − · · −·       |
| Nn       | − ·        | @            | · − − · − ·      |
| Oo       | − − −      | Error        | · · · · · · · ·  |
| Öö       | − − − ·    | <p><br></p>  | <p><br></p>      |
| Pp       | · − − ·    | Sayılar      |                  |
| Qq       | − − · −    | Sayı         | Kod              |
| Rr       | · − ·      | 0            | − − − − −        |
| Ss       | · · ·      | 1            | · − − − −        |
| Tt       | −          | 2            | · · − − −        |
| Uu       | · · −      | 3            | · · · − −        |
| Üü       | · · − −    | 4            | · · · · −        |
| Vv       | · · · −    | 5            | · · · · ·        |
| Ww       | · − −      | 6            | − · · · ·        |
| Xx       | − · · −    | 7            | − − · · ·        |
| Yy       | − · − −    | 8            | − − − · ·        |
| Zz       | − − · ·    | 9            | − − − − ·        |

1.  Tabloda verilen değerlere göre morse dönüşümü yapan fonksiyonu yazınız.

    1. metinToMorse (metin) -> morse
    2. morseToMetin (morse) -> açık metin


2.  Verilen açık metin morse ses dosyası üreten fonksiyon yazın.

    1. metinToMorseSound (metin) -> morse ses dosyası


3. Verilen ses dosyasında morse alfabesi ile ifade edilen metni bulun. Bunun için audacity yazılımını kullanabilirsiniz.

{% file src="../../.gitbook/assets/morse_gizli_bilgi.mp3" %}

{% file src="../../.gitbook/assets/morse_gizli_bilgi.midi" %}



### ANALİZ :

\


\


### REFERANSLAR :

1 – Morse Alfabesi, [https://en.wikipedia.org/wiki/Morse\_code](https://en.wikipedia.org/wiki/Morse\_code), Son erişim tarihi : 20.11.2015

2- Morse Alfabesi Ses Kütüphanesi, [https://en.wikipedia.org/wiki/Morse\_code](https://en.wikipedia.org/wiki/Morse\_code), Son erişim tarihi : 20.11.2015

### LAB KİTAPÇIĞI

{% file src="../../.gitbook/assets/Uygulama - Morse Alfabesi.docx" %}

{% file src="../../.gitbook/assets/Uygulama - Morse Alfabesi.pdf" %}
