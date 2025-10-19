import hashlib

def md5_Hash(text):
    obj = hashlib.md5()
    obj.update(text.encode())
    return obj.hexdigest()

plaintext = 'Rayhanul islam MUKUL'
hash_result = md5_Hash(plaintext)
print(f'Original: {plaintext}')
print(f'Hash Result: {hash_result}')