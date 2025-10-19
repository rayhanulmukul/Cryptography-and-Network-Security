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

# Step 1
step1 = encrypt(plaintext, 5)
print('First Transposition: ', step1)

# step 2
step2 = encrypt(step1, 7)
print('Double Transposition: ', step2)


# Recover
rec1 = decrypt(step2, 7)
rec2 = decrypt(rec1, 5)
print('Recovered Original: ', rec2)

