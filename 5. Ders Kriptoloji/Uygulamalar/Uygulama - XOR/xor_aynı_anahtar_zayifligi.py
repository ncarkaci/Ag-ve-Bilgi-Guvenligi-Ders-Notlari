import random
from PIL import Image

MODES = ["RGB", "RGBA"]

def xor(pixel, mode, key):
    red = pixel[0] ^ key[0]
    green = pixel[1] ^ key[1]
    blue = pixel[2] ^ key[2]

    if mode == "RGBA": #Need Aplha if RGBA
        return (red, green, blue, 255)
    else:
        return (red, green, blue)

# Ilk resmi yukle ve XOR islemini yap.
im = Image.open("otp1.jpeg")
im.show()
# Private key
key = []
org_len = 0

# resmi yukle
pix = im.load()

# resim x,y ebatlarini yukle
width, height = im.size

# RGB 3 boyutlu array oldugu icin genislik*3 adet random number belirleyerek private key olustur.
for x in range(0, width*height*3): 
    key.append(random.SystemRandom().randint(0, 255))

org_len = len(key)

key_count = 0
for x in range(0, width):
    for y in range(0, height):
        if key_count >= org_len:
            key_count = 0

        pix[x, y] = xor(pix[x, y], im.mode, (key[key_count], key[key_count+1], key[key_count+2]))

        key_count += 3

im.save("cipher1.jpeg")
im.show()

####### IKINCI RESIM #######
im2 = Image.open("otp2.jpeg")
im2.show()
pix2 = im2.load()
org_len = len(key)

key_count = 0
for x in range(0, width):
    for y in range(0, height):
        if key_count >= org_len:
            key_count = 0

        pix2[x, y] = xor(pix2[x, y], im2.mode, (key[key_count], key[key_count+1], key[key_count+2]))

        key_count += 3

im2.save("cipher2.jpeg")
im2.show()


###### IKI ciphertext RGB'lerini birbiri ile XOR'la.

result = Image.open("blank.jpeg")
result_pix = result.load()
for x in range(0, width):
    for y in range(0, height):
        if key_count >= org_len:
            key_count = 0

        result_pix[x, y] = xor(pix[x, y], im2.mode, pix2[x,y])

        key_count += 3

result.show()
result.save("result.jpeg")