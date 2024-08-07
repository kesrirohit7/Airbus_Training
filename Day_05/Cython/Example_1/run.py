import file1_C
import time

t1 = time.time()
res = file1_C.primeFinderCython(10000)
t2 = time.time()

print("Time taken using cython code : {}".format(t2-t1))
#print(res)
