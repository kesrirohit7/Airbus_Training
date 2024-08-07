# cython: language_level=3

def primeFinderCython(int size):
    cdef int number, x, found, amount = 0
    cdef int primes[100000]
    amount = min(amount, 100000)
    found = 0
    number = 2
    
    while found<size:
        for x in primes[:found]:
            if number%x == 0:
                break
        else:
            primes[found] = number
            found += 1
        number += 1
    return [p for p in primes[:found]]
