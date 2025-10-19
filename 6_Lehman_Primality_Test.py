import random
def lehman_primility_test(p, trials:10):
    if p < 2 or p % 2 == 0:
        return False
    for _ in range(trials):
        # a^((p-1)/2) mod p
        a = random.randint(2, p - 2)
        r = pow(a, (p - 1) // 2, p)
        if r != 1 and r != p - 1:
            return False
    return True

numbers = [random.randint(3, 1000) for _ in range(10)]
for p in numbers:
    if lehman_primility_test(p, 10):
        print(f'{p}: probably prime')
    else:
        print(f'{p} Composite')