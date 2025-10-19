def polygram_encrypt(text, block_size=3):
    out = []

    for i in range(0, len(text), block_size):
        block = text[i:i+block_size]
        out.append(block[::-1])

    return ''.join(out)

def polygram_decrypt(text, block_size = 3):
    return polygram_encrypt(text, block_size)

plaintext = "rayhanulislam"
print(plaintext)
Encrypt = polygram_encrypt(plaintext, 3)
print(Encrypt)
Decrypt = polygram_decrypt(Encrypt, 3)
print(Decrypt)