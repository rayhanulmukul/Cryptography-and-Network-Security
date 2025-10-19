def extended_gcd(a, b):
    # Extended Euclidean Algorithm
    if a == 0:
        return b, 0, 1
    else:
        gcd, y, x = extended_gcd(b % a, a)
        return gcd, x - (b//a) * y, y

def modular_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('No modular inverse')
    else:
        return x % m

p = 3557
q = 2579
n = p * q
phi = (p - 1)*(q - 1)
e = 3
d = modular_inverse(e, phi)

plaintext = 6880023  # Integer message, must be < n
print("Plaintext:", plaintext)

# Encryption: Ciphertext = plaintext^e mod n
ciphertext = pow(plaintext, e, n)
print("Cipher Text:", ciphertext)

# Decryption: Decrypted = ciphertext^d mod n
decrypted = pow(ciphertext, d, n)
print("Decrypted Text:", decrypted)