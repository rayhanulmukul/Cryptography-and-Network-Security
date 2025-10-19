def encrypt(text, width):
    while len(text) % width != 0:
        text += '_'

    result = ''
    for col in range(width):
        for row in range(len(text) // width):
            result += text[row * width + col]
    return result

def decrypt(cipher, width):
    n_row = len(cipher) // width
    result = ''
    for row in range(n_row):
        for col in range(width):
            result += cipher[col * n_row + row]
    return result.replace('_', '')

plaintext = "DEPARTMENT OF COMPUTER SCIENCE AND TECHNOLY UNIVERSITY OF RAJSHAHI BANGLADESH"
print(plaintext)
Encrypt = encrypt(plaintext, 5)
print(Encrypt)
Decrypt = decrypt(Encrypt, 5)
print(Decrypt)