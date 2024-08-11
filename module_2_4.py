
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(2, len(numbers)+1):
    for j in range(2, i+1):
        if i % j == 0 and i != j and i != 1:
            is_prime = False
            not_primes.append(i)
            break
        else:
            if i <= j:
                primes.append(i)
print('Primes:', primes)
print('Not Primes:', not_primes)
