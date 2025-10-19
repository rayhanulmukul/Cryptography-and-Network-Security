def encryption(text, key):
    result = ''
    for p, k in zip(text, key):
        if p.isalpha() and k.isalpha():
            val = (ord(p) - ord('A') + ord(k) - ord('A')) % 26
            result += chr(val + ord('A'))
        else:
            result += p
    return result

def decryption(ciphertext, key):
    result = ''
    for c, k in zip(ciphertext, key):
        if c.isalpha() and k.isalpha():
            val = (ord(c) - ord('A') - (ord(k) - ord('A'))) % 26
            result += chr(val + ord('A'))
        else:
            result += c
    return result

plaintext = "RAYMU KULDF"
key = 'XMDCLDFGHDFDFDF'
ciphertext = encryption(plaintext, key)
original_Decrypt = decryption(ciphertext, key)

print('Original: ', plaintext)
print('CipherText: ', ciphertext)
print('Decrypted: ', original_Decrypt)