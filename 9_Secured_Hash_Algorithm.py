import hashlib

def SHA_Hash(text):
    text_bytes = text.encode()

    sha1 = hashlib.sha1(text_bytes).hexdigest()
    sha224 = hashlib.sha224(text_bytes).hexdigest()
    sha256 = hashlib.sha256(text_bytes).hexdigest()
    sha384 = hashlib.sha384(text_bytes).hexdigest()
    sha512 = hashlib.sha512(text_bytes).hexdigest()
    return {
        'SHA-1': sha1, 
        'SHA-224': sha224, 
        'SHA-256': sha256,
        'SHA-384': sha384,
        'SHA-512': sha512,
    }

print(hashlib.sha256("hello".encode()).hexdigest())

plaintext = 'Rayhanul islam MUKUL'
hashes = SHA_Hash(plaintext)

for name, value in hashes.items():
    print(f'{name} : {value}')