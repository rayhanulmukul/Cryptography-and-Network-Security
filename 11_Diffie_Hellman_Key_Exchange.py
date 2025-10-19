prime = 353
primitive_root = 3

# Alice
alice_sec = 97
alice_pub = pow(primitive_root, alice_sec, prime)

# Bob
bob_sec = 233
bob_pub = pow(primitive_root, bob_sec, prime)


shared_sec_alice = pow(bob_pub, alice_sec, prime)
shared_sec_bob = pow(alice_pub, bob_sec, prime)

print(f'(Alice) Public Key, Secret Key: {alice_pub}, {alice_sec}')
print(f'(Bob) Public Key, Secret Key: {bob_pub}, {bob_sec}')
print(f'Shared Secret (Alice) : {shared_sec_alice}')
print(f'Shared Secret (Bob) : {shared_sec_bob}')