
def encrypt(text):
    out = []
    for ch in text:
        if 'a' <= ch <= 'z':
            temp = (ord(ch) - ord('a') + 3) % 26
            out.append(chr(ord('a') + temp))
        elif 'A' <= ch <= 'Z':
            temp = (ord(ch) - ord('A') + 3) % 26
            print(temp)
            out.append(chr(ord('A') + temp))
        else:
            out.append(ch)
    return ''.join(out)

def decrypt(a):
    out = []
    for ch in a:
        if 'a' <= ch <= 'z':
            temp = (ord(ch) - ord('a') - 3) % 26
            out.append(chr(ord('a') + temp))
        elif 'A' <= ch <= 'Z':
            temp = (ord(ch) - ord('A') - 3) % 26
            print(temp)
            out.append(chr(ord('A') + temp))
        else:
            out.append(ch)
    return ''.join(out)


plaintext = "abcdegh Hello"
print(plaintext)
Encrypt = encrypt(plaintext)
print(Encrypt)
Decrypt = decrypt(Encrypt)
print(Decrypt)