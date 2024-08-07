import ctypes
clib = ctypes.CDLL("/home/rohit/Desktop/Day5/Ctypes/dir_6/first.so")

values=(ctypes.c_int * 10)()

for i in range(len(values)):
    print(values[i])

# Assigning Values

print("\n*******************************************\n")

for i in range(len(values)):
    values[i] = i*2

for i in range(len(values)):
    print(values[i])

print("\n*******************************************\n")

sum = clib.getSum(values, len(values))
print("Sum = ", sum)

print("\n*******************************************\n")

clib.incArray.restype = ctypes.POINTER(ctypes.c_int)
result = clib.incArray(values, len(values))
#print(result.contents)
for i in range(len(values)):
    print(result[i])

print("\nHari Bol\n")
