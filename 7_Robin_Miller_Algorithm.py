import random
def robin_miller(p, k=5):
    if p < 2 or p % 2 == 0:
        return False
    if p == 2 or p == 3:
        return True
    # Write p - 1 = 2 ^ s * d
    d = p - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randint(2, p - 2)
        x = pow(a, d, p)
        if x == 1 or x == p - 1:
            continue
        for _ in range(s-1):
            x = pow(x, 2, p)
            if x == p - 1:
                break
        
        else:
            return False
    return True

numbers = [random.randint(2, 1000) for _ in range(10)]
for p in numbers:
    if robin_miller(p, 5):
        print(f'{p}: probably prime')
    else:
        print(f'{p} Composite')