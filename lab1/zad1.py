import math

def prime(n):
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


print(prime(2))
print(prime(3))
print(prime(10))

def select_primes(f_list):
    return list(filter(prime, f_list))

print(select_primes([1, 3, 10, 11, 49]))