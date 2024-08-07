from file1_P import primeFinderPython
import file1_C
import time


if __name__ == "__main__":
    t1 = time.time()
    primes = primeFinderPython(100000)
    t2 = time.time()
    print("Time taken using python script: {}".format(t2-t1))
    #print(primes)

    t3 = time.time()
    res = file1_C.primeFinderCython(100000)
    t4 = time.time()
    print("Time taken using cython code : {}".format(t4-t3))
    #print(res)
