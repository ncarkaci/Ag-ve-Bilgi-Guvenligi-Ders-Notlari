#!/usr/bin/env python2

from os import urandom

def genkey(length):
    """Generate key"""
    return urandom(length)

def xor_strings(s,t):
    """xor two strings together"""
    return "".join(chr(ord(a)^ord(b)) for a,b in zip(s,t))

message = 'This is a secret message'
print 'message:', message

key = genkey(len(message))
print 'key:', key

cipherText = xor_strings(message, key)
print 'cipherText:', cipherText
print 'decrypted:', xor_strings(cipherText, key)

# verify
if xor_strings(cipherText, key) == message:
    print 'Unit test passed'
else:
    print 'Unit test failed'