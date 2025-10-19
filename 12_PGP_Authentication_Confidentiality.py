
import zlib, secrets, base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA1
from Crypto.Signature import pkcs1_15
from Crypto.Cipher import DES3, PKCS1_OAEP
from Crypto.Util.Padding import pad, unpad

def b64(data, cut=40): return base64.b64encode(data).decode()[:cut]

# Key Generation
A_priv, B_priv = RSA.generate(2048), RSA.generate(2048)
A_pub,  B_pub  = A_priv.publickey(), B_priv.publickey()

# Sender
M = b"Catch Me If You Can"
S = pkcs1_15.new(A_priv).sign(SHA1.new(M))
signed = len(S).to_bytes(2,"big") + S + M
C = zlib.compress(signed, 9)

Ks = DES3.adjust_key_parity(secrets.token_bytes(16))
cipher = DES3.new(Ks, DES3.MODE_ECB).encrypt(pad(C, 8))
E_Ks  = PKCS1_OAEP.new(B_pub).encrypt(Ks)
packet = (E_Ks, cipher)

# Show stages (optional, can be omitted to shrink more!)
print("Plain:", M.decode())
print("Signature:", b64(S))
print("RSA-session:", b64(E_Ks))
print("3DES-enc:", b64(cipher))

# Receiver
Ks2  = PKCS1_OAEP.new(B_priv).decrypt(packet[0])
plain = unpad(DES3.new(Ks2, DES3.MODE_ECB).decrypt(packet[1]), 8)
recv  = zlib.decompress(plain)

slen = int.from_bytes(recv[:2],"big")
S2, M2 = recv[2:2+slen], recv[2+slen:]

try:
    pkcs1_15.new(A_pub).verify(SHA1.new(M2), S2)
    vmsg = "VALID"
except (ValueError, TypeError):
    vmsg = "INVALID"

print("Received:", M2.decode())
print("Signature check:", vmsg)
